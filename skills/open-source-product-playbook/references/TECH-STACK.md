# 技术栈选型：三条路线，自由选择

> v2.0 · 2026-11-16 · 通用，与具体产品无关。
> 配套：[MANIFESTO.md](./MANIFESTO.md)（理念与选题）· [PRODUCT.md](./PRODUCT.md)（产品完善性）· [DEV-TIPS.md](./DEV-TIPS.md)（AI 协作）· [AGENTS.md](./AGENTS.md)（如何写项目 AGENTS.md）。设计系统是独立可选轴（§3），不绑定任何栈。
>
> **AI 必读**：不要预设唯一栈。先按 §2 用产品形态定路线，再按 §3 选设计系统（可选，可不选）。三栈的开发思路都已写全，选定后垂直切片推进。

---

## 0. 选型原则

- **没有唯一最优栈，只有形态内的近优解。** 栈是选择，不是教条。
- **设计系统与技术栈正交**：选栈 ≠ 选 UI。设计系统也是选择，不是教条（§3）。
- 按产品形态与目标选，不按「哪个优雅」或「AI 最听话」选——AI 友好度是加分项，不是决定项。
- 共同底线（三栈都遵守）：垂直切片、传播单元先行、测试 / CI、PRODUCT P0 完善性、DEV-TIPS 协作纪律。

---

## 1. 三条路线（开发思路）

### 路线 A — 全栈 TypeScript

**栈**：Next.js + tRPC + Drizzle + Tailwind + shadcn/ui
**形态**：Web 应用 / 自托管服务器

**开发思路**：
- 端到端类型共享：tRPC 让前后端共用类型契约，接口几乎不会写错——这是它对 AI 最友好的地方。
- Drizzle + SQLite/Postgres 数据层，类型安全迁移。
- shadcn/ui 所有权模式：组件进仓归项目所有，headless 行为 + 自有样式。
- Tailwind 构建期产物，零运行时。
- 需要服务端时这套最顺；纯本地优先客户端可降级为 Vite SPA（去掉 SSR 死重）+ Tauri/PWA 壳。

**包体积 / 性能**：客户端 ~100–300KB gz；SSR 首屏快；富交互均衡；Node 服务端 I/O 吞吐强。
**适合**：Web 富交互 + 需要服务端 + TS 贡献池最大。
**注意**：本地优先纯客户端时 SSR 是负担；tRPC 把 API 锁在 TS 客户端，生态型服务器另暴露 OpenAPI REST。

### 路线 B — Python 全栈

**栈**：FastAPI + HTMX + Alpine.js
**形态**：服务端渲染 Web，内容 / CRUD / 数据应用

**开发思路**：
- HTML-over-the-wire：服务端直出 HTML，HTMX 局部替换，几乎不写前端框架。
- Alpine.js 处理少量客户端交互（~15KB）。
- FastAPI 异步后端；Python 是 AI 最熟的语言，代码量少、出错率低。
- 无 hydration、无虚拟 DOM，首屏即服务端 HTML。

**包体积 / 性能**：客户端 ~30KB gz（断崖式最小）；首屏最快、客户端最轻；每次交互走网络（离线弱）。
**适合**：内容站 / CRUD / 内部工具 / 数据应用，极简主义，Python 团队。
**注意**：富动画 / 离线场景弱；Reflex / Streamlit 是更重的另一回事（Streamlit 整脚本重跑，Reflex 底层是 React），别混为一谈。

### 路线 C — Flutter

**栈**：Flutter + Riverpod + GoRouter
**形态**：原生跨平台 APP（Android / iOS / 桌面 / web）

**开发思路**：
- 声明式 Widget 当「AI 画布」：快速生成跨平台 UI，不追求完美原生。
- Riverpod 状态管理，GoRouter 声明式路由。
- 一份代码编译到多平台原生；AOT 编译成机器码。
- 设计系统有官方支持（MD3 的 `material_ui` 包等），是三者中唯一有官方现成设计组件的。

**包体积 / 性能**：原生包基线 ~5–8MB（Android arm64，自带渲染引擎）；UI 动画最流畅（Impeller 60/120fps）；离线原生响应。
**适合**：跨平台原生 APP、富交互 / 动画、离线优先。
**注意**：包基线大（引擎开销）；Flutter web 渲染引擎重（~2–4MB）；Dart 训练数据少于 TS。

---

## 2. 选型决策（按目标，不按优雅）

| 目标 | 推荐 |
|---|---|
| 轻量 Web 工具 / 内容站 / 内部 CRUD | B |
| Web 富交互 + 服务端 + TS 生态 / 贡献池 | A |
| 跨平台原生 APP / 富动画 / 离线优先 | C |
| 本地优先桌面应用 | A 降级 Vite+Tauri，或 C |
| 自托管服务器 + 开放 API 生态 | A（tRPC 给自家 UI + OpenAPI REST 给生态） |

判据一句话：**按产品形态与未来贡献者会什么选。** AI 友好度三栈都高，不构成决定差异。

---

## 3. 设计系统：独立可选轴（不绑定任何栈）

**设计系统 ≠ 技术栈。** 选栈不等于选 UI；设计系统是正交的第二次选择，而且可以不选。

三大设计语言详解见 [UI-DESIGN.md](./UI-DESIGN.md)。

| 选项 | 说明 |
|---|---|
| Material 3 Expressive | Google / Android；表现力 + 动态取色。Flutter 官方组件，Web 需自写（UI-DESIGN §1） |
| Fluent 2 | Microsoft / Windows / M365；克制 + 材料层次。Web 有成熟组件库（UI-DESIGN §2） |
| Liquid Glass / Apple HIG | Apple / iOS / macOS；通透流体 + 内容优先。Web 仅视觉近似（UI-DESIGN §3） |
| 自定义 token 体系 | 自有品牌；token 单一来源 |
| 无（原生朴素） | 直接用平台默认控件，最轻 |

**无论选哪个（或不选），共同纪律**：
- 若选设计系统：token 单一来源（JSON → 各平台），不绑定重型组件框架，原生 HTML/CSS 优先，headless 借行为。
- 设计系统是选项，不是教条——不要为了「统一」强行套一个不适合产品形态的系统。
- **任何设计语言都只是选项之一，不是必选，更不是唯一答案。**

---

## 4. 三栈共享的工程纪律

- 垂直切片：每片完整可用，不留 TODO。
- 传播单元先行：最早做出 hero 截图，用它校准方向（MANIFESTO §5）。
- 测试 / CI / 视觉回归；PRODUCT.md P0 完善性全项。
- monorepo 边界清晰；一键启动 + 种子数据；DEV-TIPS 协作纪律。
- 业务引擎与 UI 解耦，便于换栈 / 换壳。

---

## 5. 包体积与性能速查（近似数量级）

| 轴 | A (Next.js) | B (HTMX) | C (Flutter) |
|---|---|---|---|
| 客户端 JS 载荷 | ~100–300KB gz | ~30KB gz（最小） | ~2–4MB（web 引擎） |
| 原生安装包 | 不直接产出 | 不直接产出 | ~5–8MB 起（Android） |
| 桌面装壳 | Tauri ~3–10MB / Electron ~100MB+ | Tauri ~3–10MB | ~15–30MB |
| 首屏 / 客户端轻量 | SSR 快 | 最快最轻 | 引擎启动稍慢 |
| 富动画 / 离线 | 中 | 弱 | 最强 |
| 服务端吞吐 | Node 强（I/O） | FastAPI 强（I/O） | — |

**结论**：客户端最小 = B；原生 APP 性能 / 动画最强 = C（代价包大）；Web 富交互均衡 = A。没有全能冠军，按形态选。