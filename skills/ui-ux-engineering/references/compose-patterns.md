# Compose 实现与测试

先确认项目真正解析的依赖和支持的平台。旧版项目优先用已有 API 做出意图，必要升级说明哪项交互会受益和要验证的兼容性。下面的 API 按项目已解析版本及目标平台核实。[Material 3 版本记录](https://developer.android.com/jetpack/androidx/releases/compose-material3)

## 状态、布局与输入

- **一次动作，一个状态来源。** 提交防重放在动作处理处，同时给用户可见反馈。加载中的请求应能区分新旧结果，避免迟到的结果覆盖更新内容。刷新失败可以与已加载内容并存。Android 可在现有架构中用 `collectAsStateWithLifecycle` 订阅 Flow。用 `rememberSaveable` 或现有状态持有者保存选中 ID、查询词和少量未提交输入，搜索结果或大对象由数据层重取。
- **列表位置跟着条目。** 用业务 ID 作为列表稳定 key。长列表或复杂列表用已有惰性布局，异构条目适合提供 `contentType`。返回列表、刷新和切换布局时检查当前条目与滚动位置。真实位置变化确实影响读者理解时，用支持的 `animateItem` 保持连续。
- **判断实际窗口。** 用现有窗口尺寸分类和布局组件选择单栏或多栏，在折叠、分屏或桌面窗口大小变化时保留选中项。处理 `Scaffold` 内容 padding 与系统 insets 的消费，避免系统栏或 IME 重复加空白。把 Android 专属生命周期和返回手势留在对应平台。
- **保留原生语义。** 标准按钮、选择控件和菜单先用库组件。自绘控制要补可访问名称、角色、状态和操作。确认 Tab、返回和弹层关闭后的焦点。键盘与辅助技术也应能执行关键动作。

[状态恢复](https://developer.android.com/develop/ui/compose/state-saving) · [惰性列表](https://developer.android.com/develop/ui/compose/lists) · [系统 insets](https://developer.android.com/develop/ui/compose/system/insets-ui) · [语义](https://developer.android.com/develop/ui/compose/accessibility/semantics)

## 选对动效机制

| 要解决的问题 | 实现思路 |
|---|---|
| 普通控件状态变了 | 先保留组件已有反馈。状态驱动、可中断的空间变化可用 spring，透明度或颜色用简短的过渡。 |
| 用户直接拖动或甩动 | 优先用组件已有的拖拽、滚动物理或合适的锚点 API。自定义时由一个状态持有位移，重抓取消旧动画。松手时用 `VelocityTracker` 取得速度，可用 `Animatable.animateTo` 的 `initialVelocity` 吸附，或用 `animateDecay` 延续惯性。根据速度、目标和取消规则决定是否提交。 |
| 同一对象在布局或页面之间移动 | 同一对象重排可考虑 `LookaheadScope` 内的 `animateBounds`。跨页保留同一元素可用 `sharedElement`，内容不同但共用容器的变换可用 `sharedBounds`。检查返回、快速来回点与元素已经移出屏幕的情形。 |

手势取消、改向和减少动效时都要能继续操作。滚动和可滑动行共存时，试纵向划动和横向滑动。开始滑动时记住条目 ID，提交前按当前数据核对，刷新移除条目时取消动作。触觉反馈可用于提交或达到手势目标。

[Compose 动画指南](https://developer.android.com/develop/ui/compose/animation/quick-guide) · [Animatable](https://developer.android.com/reference/kotlin/androidx/compose/animation/core/Animatable) · [布局动画](https://developer.android.com/reference/kotlin/androidx/compose/animation/animateBounds.modifier) · [共享元素](https://developer.android.com/develop/ui/compose/animation/shared-elements)

## 诊断卡顿

先复现指定动作和时间点。测输入后第一次可见反馈、数据最终状态和帧表现，判断瓶颈是在等待数据，还是主线程、布局或绘制。对于高频的纯视觉变化，在布局或绘制需要它的时候再读状态，避免每帧重组整页。需要改变内容测量时按实际布局处理。

有性能验收要求时，尽量用同一实体设备、同样数据与构建模式做前后对照。用接近发布版、支持性能分析的构建。在已有 Macrobenchmark 里可用 `FrameTimingMetric`，少数帧特别慢时用 Perfetto 查时间线。只有模拟器或单次录屏时，记录观察结果和设备范围。[Compose 性能](https://developer.android.com/develop/ui/compose/performance) · [Macrobenchmark 指标](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-metrics)
