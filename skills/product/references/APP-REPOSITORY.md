# 开源 App 的 GitHub 仓库

适用于移动端、桌面端或带安装包的开源 App。把 README 做成用户和贡献者的入口。读者从首页就能判断 App 有什么用、设备能否运行、怎样拿到正确的版本，以及出了问题去哪里。只整理 README 时，交付范围为所需文案、展示素材和链接与渲染检查。项目设置、工作流和发布按实际任务范围处理。

## 从 Kazumi 学到的维护方式

核对于 2026-11-25，源版本 `3ae13bf`。Kazumi 根目录唯一的 Markdown 文件是 `README.md`。它把较长的贡献与结构说明放在 `static/doc/`，截图放在 `static/screenshot/`，下载徽章放在 `static/svg/`。运行时资源另有 `assets/`。复杂安装和规则开发已有官网文档，README 在读者用到时链接过去。[仓库树](https://github.com/Predidit/Kazumi/tree/3ae13bfba2cc9bcd727807e8115f93e29e75004b) · [README](https://github.com/Predidit/Kazumi/blob/3ae13bfba2cc9bcd727807e8115f93e29e75004b/README.md) · [官网文档](https://kazumi.app/docs/)

贡献指南由 README 和 PR 模板共同指向。问题表单区分反馈类型，并给社区帮助入口。PR 检查和正式发布使用不同工作流，正式版本的说明和安装文件集中在 Releases。这些位置各自承担一件事，入口清楚，更新时也容易找准要改的地方。[贡献指南](https://github.com/Predidit/Kazumi/blob/3ae13bfba2cc9bcd727807e8115f93e29e75004b/static/doc/CONTRIBUTING.md) · [PR 模板](https://github.com/Predidit/Kazumi/blob/3ae13bfba2cc9bcd727807e8115f93e29e75004b/.github/PULL_REQUEST_TEMPLATE.md) · [问题表单](https://github.com/Predidit/Kazumi/tree/3ae13bfba2cc9bcd727807e8115f93e29e75004b/.github/ISSUE_TEMPLATE) · [工作流](https://github.com/Predidit/Kazumi/tree/3ae13bfba2cc9bcd727807e8115f93e29e75004b/.github/workflows) · [Releases](https://github.com/Predidit/Kazumi/releases)

## 仓库目录

- **根目录的 Markdown 默认只有 README。** 单语言用 `README.md`。中英双语按默认语言配 `README.zh-CN.md` 或 `README.en.md`，两份互链并共用图片，保持平台、下载和贡献信息一致。已有命名约定就沿用。照常保留 `LICENSE`、源码和构建配置。
- **仓库素材统一放 `static/`。** `static/doc/` 放 README 链接到的较长 Markdown，例如贡献指南或目录说明。用 `static/svg/` 存项目有权维护的 SVG 徽章和图标，用 `static/screenshot/` 存正式截图，其余展示图片可放 `static/images/`。只有实际需要才建子目录。素材用 Git 相对路径，应用已经打包的同一张图可直接引用原文件。
- **GitHub 专用文件放 `.github/`。** Issue 表单、PR 模板和工作流各用自己的位置。贡献规则简单时留在 README。内容较长时从 README 和 PR 模板链接到同一份指南。需要 GitHub 自动识别时可用 `.github/CONTRIBUTING.md`。[GitHub README 指南](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) · [贡献指南识别位置](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- **沿用已有入口。** 默认通过 README、静态附件和项目已有站点承载文档。版本变更集中在实际发行渠道。已有仓库保留外部已链接、构建已使用和平台必须识别的路径。用户要求迁移时，核对工具配置和入站链接，并更新需要随文件迁移的入口。

## README 页首

用一个居中的简介区，下面正文正常左对齐。顺序为**应用名 → 应用图标 → 实际存在的 TrendShift 等展示 → 可点击的徽章 → 简短介绍**。双语切换可以放在介绍之后。

- 应用名用一个一级标题。图标用项目自己的图，控制尺寸，让手机上仍能很快读到简介。
- 有真实的 TrendShift 项目页或其他推荐记录时展示，需要时核对徽章和目标页。社群可用带 Telegram 等品牌标识的可点击徽章。入口优先给下载、社群或常用帮助，技术和状态徽章按实际信息取舍。每枚链接徽章的替代文本要说清点过去能做什么。
- 简介用几句话交代产品做什么、主要能力或差异以及当前状态。短一点也可以有作者自己的语气。只写项目已具备的能力。

居中的基础结构可以这样写，实际出稿时换成项目的内容。有真实来源、有对应素材时，再在图标和社群入口之间插入 TrendShift。

```html
<div align="center">
  <h1>应用名称</h1>
  <p><img src="static/images/app-icon.png" width="128" alt="应用图标"></p>
  <p><a href="项目实际社群地址"><img src="static/svg/telegram.svg" alt="加入 Telegram 社群"></a></p>
  <p>一句话说明这款应用做什么，再补一两项实际能力。</p>
</div>
```

## README 正文顺序

| 段落 | 写给读者的内容 |
|---|---|
| 支持平台 | 平台、最低版本及会影响安装的架构或限制。实验支持、侧载、分支项目等状态写在对应平台旁。 |
| 屏幕截图 | 用真实界面展示最有代表性的任务。采用同一组视觉尺度，标清场景并写替代文本。图多时试窄屏布局。 |
| 功能与开发计划 | 区分现在能用的功能与待办。尚无公开计划时列已验证功能。项目已在 Issues 或 Projects 维护路线图时，从这里链接过去。 |
| 下载 | 把 Releases 和实际商店、包管理器入口按平台排清楚。说明用户该选什么格式或架构，安装复杂时链接到已有教程。README 不维护逐版安装包列表。 |
| 贡献 | 说清可贡献什么。若有构建前置条件、评审规则或较长步骤，把入口连到同一份贡献指南。 |
| 问题与帮助 | 给出可用的问题入口，并用短 FAQ 解决反复出现的疑问。问题多时按读者或场景折叠，安装和下载关键信息保持可见。 |
| 适用的补充 | 有实际内容再写美术与字体来源、免责声明、隐私、代码签名、赞助或致谢。区分源码协议和图片、图标、字体的来源与授权，按项目实际情况表述。 |

## 日常维护

- 发布页负责版本号、用户可见变化和安装文件。核对 README、发行说明、平台和产物名称相符。签名说明以确实执行的流程为准，写清哪些平台或产物已签、由谁负责以及需要的用户步骤。按渠道分别验证安装包，明确标注未签名或仅有预览的产物。[GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- 反馈表单只收能帮助复现的字段，例如版本、系统、步骤、预期和实际结果。日志或截图提醒先清理隐私信息。PR 模板提示改动、关联问题和验证结果，可指向实际的 AI 使用约定。提交检查和需要发布权限的工作流根据项目实际规模和权限分开设置。[GitHub 模板指南](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates)
- 交付前从 GitHub 首页走一遍。确认首屏说清产品是什么，宽屏和窄屏都可读。逐个核对语言切换、徽章、截图、下载、贡献与反馈的链接，同时比对两份 README 共享的事实。用自己的文案和有权使用的素材呈现。
