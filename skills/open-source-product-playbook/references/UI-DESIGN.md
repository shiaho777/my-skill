# UI 设计系统：三大设计语言，自由选择

> v1.0 · 2026-11-16 · **可选轴，三选一（或不选）。** 本文替代原 MD3-UI.md。
> 配套：[TECH-STACK.md](./TECH-STACK.md) §3（设计系统选型）· [MANIFESTO.md](./MANIFESTO.md) · [PRODUCT.md](./PRODUCT.md) · [DEV-TIPS.md](./DEV-TIPS.md) · [AGENTS.md](./AGENTS.md)。
>
> **AI 必读**：设计系统独立于技术栈，按目标平台与产品气质选，不强制。三者都活跃演进中，没有「被时代抛弃」的那个。数值截至 2026-11-16，采纳前复核；标注 [待核] 的条目未从一手来源证实。

---

## 0. 定位与选型

**设计系统 ≠ 技术栈。** 选栈不等于选 UI；这是正交的第二次选择，而且可以不选。

| 设计语言 | 生态 | 当前形态 | 气质 |
|---|---|---|---|
| Material 3 Expressive | Google / Android / web | M3 Expressive（2025） | 表现力、情感、动态取色 |
| Fluent 2 | Microsoft / Windows / M365 | Fluent 2 + Fluent UI v9 | 克制、生产力、材料层次 |
| Liquid Glass / Apple HIG | Apple / iOS / macOS | Liquid Glass（2025） | 通透、流体、内容优先 |

**选型判据**：目标平台的原生感 → 产品气质 → 跨平台策略。也可自定义 token 体系，或干脆不选（原生朴素，最轻）。

**三者共同点**：都已 token 化、都重无障碍、都有官方组件库、都在 2025–2026 持续演进。

---

## 1. Material 3 Expressive（Google）

**定位**：M3 的 opt-in 扩展层，不是 M4，不废弃基线 M3。本质是把情感设计变成可工程化的 token 系统。

**运动物理**（范式：可中断、可重定向、继承速度的弹簧，取代贝塞尔时长）：

| Token（damping / stiffness） | Expressive | Standard |
|---|---|---|
| spatial fast / default / slow | 0.6/800 · 0.8/380 · 0.8/200 | 0.9/1400 · 0.9/700 · 0.9/300 |
| effects fast / default / slow | 1.0/3800 · 1.0/1600 · 1.0/800 | 同左 |

Spatial（位置/尺寸/形状）允许超调；Effects（颜色/透明度）绝不超调。颜色动画误用 spatial 会超调——错误。

**形状**：35 形状库任意互变；10 档角标尺 0/4/8/12/16/**20**/28/**32**/**48**/full（粗体为新增）。形状非语义，编码注意力。

**排版**：30 样式 = 15 baseline + 15 emphasized（同 scale 位加字重）；token 交换启用，组件默认不用；不用于正文/标签。

**色彩**：真实变更是三级对比度 token（standard / medium ≥3:1 / high 7:1），明暗自动。「vibrant」是话术，无新 scheme 变体。MCU：`SchemeExpressive` + `contrastLevel −1..1` + `SpecVersion 2025/2026`。

**组件（5 新 + 9 改）**：新 Button groups（取代 segmented）/ FAB menu（取代 speed dial）/ Loading indicator / Split button / Toolbars（docked 取代 bottom app bar）；改 App bars / Common buttons / Extended FAB / FABs / Icon buttons / Navigation bar / Navigation rail（expanded 取代 drawer）/ Progress indicators（波浪+厚度）/ Sliders。

**战术（7 条）**：形状多样性 / 丰富色彩 / 排版引导 / 容器分组 / 流体动效 / 组件灵活 / 组合 hero moment（只留 1–2 个）。

**护栏**：对比度三级是无障碍基础设施；reduced-motion 必须降级；场景敏感（金融/工具克制）。

**平台与 Web 映射**：Compose 1.5 线（rc01，2026-11）逐个毕业；Flutter `material_ui` 部分落地；**Web 无官方 Expressive 实现，需自写**——弹簧用 `linear()` 采样近似（`spring()` 未发布），形变用 `shape()`/clip-path，强调体用可变字重，取色用 MCU。

---

## 2. Fluent 2（Microsoft）

**定位 / 生态**：Microsoft 当前设计系统，用于 Windows 11、Microsoft 365、Teams、Outlook。Fluent UI 是其代码实现族（MIT）。

**材料**（四种）：solid（实色）/ **mica**（不透明，取用户壁纸着色，窗口失焦转中性；采样壁纸一次，性能友好）/ **acrylic**（半透磨砂玻璃，用于瞬态面如菜单/弹层，GPU 重，省电模式自动关）/ **smoke**（模态下的半透黑遮罩）。

**形状**：设计站圆角 None 0 / Small 2 / Medium 4 / Large 8 / XL 12 / Circle 50%。[待核] 代码 token 与设计站有出入（代码 `borderRadiusLarge`=6px，8px 是 `XLarge`）——以代码 token 为准。Windows 11：顶层窗口/弹层 8px，页内控件 4px。

**层级**：shadow 2/4/8/16（低，卡片/FAB/命令栏）+ shadow 28/64（高，侧栏/对话框）；key（锐利定向）+ ambient（柔和漫射）双阴影；Windows 用描边替代 key 阴影。彩色表面用品牌阴影，不用主 ramp。

**排版**：Windows 用 Segoe UI Variable（光学尺寸 small/text/display），web 用 Segoe UI，macOS/iOS 回退 SF Pro，Android 回退 Roboto。ramp 10–68px（Caption2 10 → Display 68）；字重 Regular 400 / Medium 500 / Semibold 600 / Bold 700。对比：正文 ≥4.5:1，大字 ≥3:1。

**色彩**：三 palette——neutral（表面/文本）/ shared（跨 M365 语义色，红=危险/黄=警示/绿=正向）/ brand（每产品自有）。light/dark/high-contrast 主题；brand 主色 #0078d4（hover #106ebe / pressed #004578）。焦点用加粗描边而非变色。

**动效**：duration 50–500ms（UltraFast 50 → UltraSlow 500）+ 曲线族（EasyEase / Accelerate / Decelerate）；原则功能性、自然（惯性/重力）、一致；支持「无动效」设置。

**Token 架构**：global（原始值）+ alias（语义、上下文感知）两层，原生支持 light/dark/high-contrast/brand。[待核] 「control tokens」非文档正式第三层；v9 组件直接消费 alias/global + 局部 CSS 变量。

**组件库（截至 2026-11）**：

| 库 | 包 | 版本 | 状态 |
|---|---|---|---|
| React v9 | `@fluentui/react-components` | 9.75.2 | stable，M365 主用，Griffel 近零运行时 |
| Web Components | `@fluentui/web-components` | 3.2.1 | stable v3，Edge 主用，框架无关 |
| Blazor | `Microsoft.FluentUI.AspNetCore.Components` | 5.0.1 | 活跃 v5（社区支持） |
| Apple | `FluentUI`（SPM） | 0.37.0 | UIKit/AppKit + SwiftUI，已支持 iOS 26 Liquid Glass |

**Web 用法**：React 应用用 v9（`FluentProvider` + theme，Griffel 原子 CSS 去重，相对轻）；非 React 用 web components。**Fluent 是三者中 web 上唯一有成熟现成组件库的。** Northstar（v0）已于 2025-07 EOL。

---

## 3. Liquid Glass / Apple HIG（Apple）

**定位**：WWDC 2025-06-09 发布，2025-09-15 随 iOS 26 / iPadOS 26 / macOS Tahoe 26 / watchOS 26 / tvOS 26 / visionOS 26 正式推送——Apple「史上最广的软件设计更新」，首次跨平台统一设计语言。

**材质**：通透玻璃，反射/折射周围环境，色彩取自邻近内容并自适应明暗；**实时渲染**，随运动产生镜面高光，按内容/上下文形变。

**变体与应用层**：
- **Regular**：模糊并调整背景亮度，多数系统组件用；用于 alert/侧栏/弹层/文本密集区。
- **Clear**：高透，仅用于富视觉背景（照片/视频）之上；亮背景上考虑加 35% 暗化层。
- **纪律**：Liquid Glass 只用于**功能/导航层**（tab bar / nav / toolbar / 控件），**不在内容层**；**克制使用**；框架组件自动采用。

**SwiftUI API**（26.0 起）：`.glassEffect(.regular/.clear, in: shape)`（默认 capsule）；`Glass.interactive()` / `.tint()`；`GlassEffectContainer`（合并多个玻璃形状并互相形变，spacing 越大越早融合）；`glassEffectID(_:in:)`（跨转场 morph 身份）；`.buttonStyle(.glass)`。规则：glassEffect 放在其他外观修饰器之后；容器/效果过多会掉性能。[待核] SwiftUI glassEffect 可用性列表不含 visionOS（visionOS 用自有自适应材质）。

**排版 / 圆角**：SF Pro（iOS/macOS 等）/ SF Compact（watchOS）；动态字级（macOS 不支持 Dynamic Type）；连续曲率圆角（`RoundedCornerStyle.continuous`，俗称 squircle）。2025-12 HIG 为 Dynamic Type 加了强调字重。

**可读性争议与护栏**：透明度伤文本对比/可读性（尤其阳光下）引发批评；Apple 逐步调整——beta 期提高不透明度，**iOS 26.1（2025-11）加入用户透明度控制**，**WWDC26 提供滑块从 ultra-clear 到 fully tinted 自定义**。无障碍：Reduce Transparency / Increase Contrast 自动适配材质。[待核] 具体设置标签与点名退出的 App 未从一手证实。

**Web 近似**：CSS `backdrop-filter: blur() saturate()`（元素背景须半透），Baseline newly available（2024-09 起）。**陷阱**：祖先若有 filter/opacity<1/mask/clip-path/backdrop-filter 等会成为 backdrop root，裁掉模糊可见范围。**局限**：CSS 只有模糊+着色，无折射/镜面高光/形状形变/自动亮度适应——只能视觉近似，非真材质。

**当前状态**：iOS 27 / macOS 27（2026）继续精修（更低默认透明度、统一工具栏、边到边侧栏）。第三方如 Fluent UI Apple 0.37.0 已为原生控件接入 iOS 26 玻璃。

---

## 4. 共同纪律（无论选哪个，或不选）

- **token 单一来源**（JSON → 各平台），不绑定重型组件框架，原生 HTML/CSS 优先，headless 借行为。
- **一致性锁**：token lint（禁硬编码色值/圆角）/ 视觉回归 / 跨平台测试向量。
- **无障碍护栏**：对比度 / reduced-motion / 触控目标，三者都有对应机制。
- **设计系统是选项，不是教条**——不要为了「统一」强行套一个不适合产品形态的系统。任何设计语言都只是选项之一，不是必选，更不是唯一答案。

---

## 5. 跨栈适配矩阵

| 设计语言 | Flutter（栈 C） | Web（栈 A/B） | 原生 |
|---|---|---|---|
| MD3 Expressive | 官方 `material_ui`（部分） | 自写 + token / headless | Android 原生 |
| Fluent 2 | Fluent UI Apple 近似 / 自写 | **Fluent UI React v9 / web-components 现成** | Windows 原生 |
| Liquid Glass | 自写近似 | `backdrop-filter` 视觉近似（有局限） | iOS/macOS 原生 SwiftUI |

**要点**：Fluent 是 web 上唯一有成熟现成组件库的；MD3 在 web 需自写（Flutter 有官方）；Liquid Glass 在 web 只能视觉近似，原生才有真材质。

---

## 6. 选型决策

| 目标 | 推荐 |
|---|---|
| Android 优先 / 动态取色 / 表现力 | MD3 Expressive |
| Windows / 生产力 / 企业 | Fluent 2 |
| iOS/macOS 优先 / 苹果生态原生感 | Liquid Glass |
| 跨平台一致 + 官方组件最省 | MD3（Flutter）或 Fluent（web） |
| 自有品牌 | 自定义 token 体系 |
| 最轻 | 不选，原生朴素 |

---

> 时效与来源：数值截至 2026-11-16，抓取自 m3.material.io、fluent2.microsoft.design、github.com/microsoft/fluentui、developer.apple.com、apple.com/newsroom、MDN。标注 [待核] 者未从一手来源证实，采纳前复核。