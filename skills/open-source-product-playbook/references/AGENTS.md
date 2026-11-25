# AGENTS.md 元指南：如何为项目写 AGENTS.md

> v1.2 · 2026-11-18 · **本文不是某个项目的 AGENTS.md，而是教 AI 在开发过程中为该项目写 / 维护 AGENTS.md 的元指南。** AGENTS.md 是活文档，不是固定模板。v1.1 新增交付流程（Issue → PR → main → CI → merge）写法与模板段；v1.2 新增产出物语言默认英文约定。
> 配套：[MANIFESTO.md](./MANIFESTO.md) · [TECH-STACK.md](./TECH-STACK.md) · [UI-DESIGN.md](./UI-DESIGN.md) · [PRODUCT.md](./PRODUCT.md) · [DEV-TIPS.md](./DEV-TIPS.md)。
>
> **AI 必读**：为项目写 AGENTS.md 时，只写**项目特有的、agent 会反复搞错的**约定，不写通用百科。具体、命令式、可判定，能用机器执行的别只写散文。随项目演进持续更新。
>
> **语言默认**：本套文档以中文书写只是元文档的写作语言，不代表产出物用中文。项目产出物——README、仓库描述与 topics、项目文档、commit message、PR/Issue 标题与正文——**默认一律英文**，除非用户明确指定其他语言。

---

## 0. 实证：优质项目怎么写

| 项目 | agent 文档 | 形态 |
|---|---|---|
| web-to-app | AGENTS.md（46KB） | 单体，13 个「变更食谱」占 40% |
| read-aware | CLAUDE.md 真身 + AGENTS.md symlink | 单一真源 + 技能 |
| folia-major | AGENTS.md + CLAUDE.md 指针 | 薄路由 + 14 个 SKILL.md + 机器边界检查 |
| dsh-Go | AGENTS.md 真身 + CLAUDE.md symlink | 硬规则 + 5 技能 + 真机验证 |
| BiliDesk | 无（只有 README） | — |
| Kazumi | 核对的快照中无根目录 agent 文档 | AI 贡献要求由 PR 模板和 `static/doc/CONTRIBUTING.md` 承担 |

**结论**：agent 文档不是装饰，是把硬约定机器化执行、降低 agent 错误率的工具。没有它的项目（BiliDesk/Kazumi）靠人类审查兜底；有它的项目把规矩写进 gate。

---

## 1. 核心原则（从实证提炼）

1. **项目特有，不写百科。** 模型已知的通用知识不写；只写本项目架构边界、exact 命令、禁区、高频变更步骤——agent 无法推断或会反复犯错的。
2. **具体、命令式、可判定。** 「注意性能」不是规则；「列表 >200 条必须虚拟化，CI 用 5000 条验证」才是。命令必须可复制执行。
3. **机器执行优于散文。** 规则背后要有 gate：边界检查器、注册表、parity 测试、只缩不涨的 baseline。folia 用 Dedicatus 查依赖方向，web-to-app 用 `checkConfigFieldDrift`，dsh-Go 用 `pins.json` 注册补丁。
4. **活文档。** 随架构 / 约定演进；stale 的 AGENTS.md 比没有更糟（误导 agent）。
5. **单一真源。** AGENTS.md 为真身，CLAUDE.md 用 symlink 或一行指针指向它，零漂移（read-aware/dsh-Go 实证）。
6. **Hub-and-spoke（按规模）。** 大项目：薄 AGENTS.md 路由 + 按需加载 `skills/<name>/SKILL.md`；小项目可单体。不全量塞上下文。
7. **根因 + 反过度工程。** 「Fix root causes, not symptoms」（web-to-app）；「过度防御也是缺陷——这个分支挡住的事情，真的会发生吗」（dsh-Go）。禁止投机性 fallback / 静默吞错。
8. **验证诚实。** 执行证明而非阅读；「green CI ≠ 真机正确」（dsh-Go）；「工具声称已完成不能代替人工验证」（folia）。报告实际命令与结果。
9. **人类责任不可转移。** AI 写的代码，提交者必须读懂、验证、负责（六项目共识）。

---

## 2. 标准骨架

 recurring 结构（四项目共有）：

```
项目概览 + 架构地图（repo layout + 依赖方向）
命令（build / test / lint / verify，exact）
硬规则（Do / Don't，项目特有禁区）
产出物语言（默认英文，用户明确指定除外）
架构边界（依赖方向规则 + 对应 gate）
变更食谱（高频操作的标准步骤）
工作流与 Git 安全
交付流程（Issue → PR → main → CI → merge）
安全 / 隐私
验证（risk-matched 执行证明）
技能索引（大项目，按需加载）
```

---

## 3. 每一节怎么写（实证例句）

**架构边界 → 写成依赖方向规则**：
- 「stores/utils/types/services 永不依赖 components」（folia）
- 「在线歌曲只走 omni.ts」「加一个平台只动它的文件夹 + 注册表，不开新 App.tsx 分支」（folia）
- 「edit the source, never the emitted .js」（read-aware）
- 「host 编辑器在 app/，运行时模板在 shell/ 由 Gradle 同步——直接改 shell/src 是错的」（web-to-app）

**命令 → exact + 注明陷阱**：
- 「CI 只编译 debug shell，release/R8 改动必须本地验证」（web-to-app）
- 「大多数命令禁用 configuration cache」（web-to-app）
- 每条命令可复制；标明工作目录与前置。

**硬规则 → 项目特有禁区**：
- 「代码里不写任何注释」（web-to-app）
- 「已发布的存储键不改名」（folia，注册表 + 快照测试）
- 「音乐平台库钉死版本，不写 ^ 或 ~」（folia）
- 「默认架构不放 embeddings/向量库」（read-aware）

**产出物语言 → 默认英文，写成显式规则**：本套元文档是中文，AI 容易误推断产出物也该用中文——必须在项目 AGENTS.md 里显式写死默认值：README、仓库描述与 topics、项目文档、commit message、PR/Issue 标题与正文一律英文；仅当用户明确指定其他语言时才切换，且只对该次指令生效。开源面向全球贡献池（MANIFESTO §0），英文是社区默认语言；面向中文用户的 i18n 翻译件不受此限。

**变更食谱 → 高频改动标准步骤**：web-to-app 用 13 个编号食谱覆盖常见改动（占全文 40%）。把「加一个编辑器 flag 要走 model→export JSON→shell config→runtime 且序列化命名一致」这类易错链路写成步骤。

**反过度工程**：错误只有两种结局——可恢复的动作，或显式失败；绝不静默吞或无限重试。新增状态 flag 必须写明谁设谁清、清不掉怎么办（dsh-Go）。

**Git 安全**：不主动 commit/push/PR/tag/release，除非明确要求；「只暂存明确路径，不用 git add . / -A」（dsh-Go）；保留无关 worktree 改动；不用 agent 命名空间分支（如 codex/…）；main 不 force-push。

**交付流程 → 写成可判定的闭环规则**：Issue 先行 → PR 进 main（带 `Fixes #N`）→ CI 绿灯才合并 → 合并才关 Issue。每条都要可判定：「CI 红不合并」「PR 打开时不关 Issue」「required checks 写真实 job id，不编造」。与 Git 安全分工：Git 安全管「什么时候允许动仓库」，交付流程管「动了之后怎么走完闭环」。模板见 §8。

**验证**：按风险匹配检查；运行时验收要跑真实应用，浏览器检查只覆盖布局，CSP/打包要打包构建（read-aware）；真机能力必须真机验证（dsh-Go）。

**生成物**：不手改，改输入重跑生成器（folia/dsh-Go/read-aware/web-to-app 共识）。

**安全 / 隐私**：永不 log 凭据/token/cookie；secrets/keystore 不进仓；Electron contextIsolation 开 / nodeIntegration 关（folia）；诊断包分享前人工审阅。

---

## 4. Hub-and-spoke vs 单体（按规模选）

- **小项目**：单体 AGENTS.md（web-to-app 式），但控制长度，食谱化。
- **大项目**：薄 AGENTS.md 路由 + `skills/<name>/SKILL.md`（folia 14 / dsh-Go 5 / read-aware / GoogleChrome）。每条任务只加载相关技能。
- **CLAUDE.md → symlink AGENTS.md**（或一行指针），维护一份共享指令，零漂移。
- 技能本身也要自包含、命令式（DEV-TIPS §1）。

---

## 5. 何时写 / 何时更新（活文档）

- **项目初始化**：用户明确要求，或仓库已有 agent 规范约定时，在工具能发现的位置写骨架（概览、命令、基本边界）。普通 App 的公开入口见[开源 App 仓库指南](APP-REPOSITORY.md)。
- **加模块 / 功能**：补架构边界 + 变更食谱。
- **约定变更**：同步更新，删过时规则。
- **agent 反复犯错**：把纠正固化为规则 + gate（这是 AGENTS.md 增长的主要来源）。
- **每次 PR 后反思**：有没有该固化的约定？有没有该缩的 baseline？

---

## 6. 与本套 skill 的衔接

AGENTS.md 是**项目本地实例化**：把 MANIFESTO 的理念、TECH-STACK 选定的栈、UI-DESIGN 选定的设计系统、PRODUCT 的 P0、DEV-TIPS 的纪律，落成本项目的具体约定。

- **引用而非复制**：链接到权威文档，细节不重复（dsh-Go：「每条规则保持自包含，细节链接到权威文档」）。
- 例：本项目选了栈 C + MD3 → AGENTS.md 写明 Flutter 命令、material_ui 用法、token 单一来源纪律、形变/弹簧的验证方式。

---

## 7. AI 提交政策（放 CONTRIBUTING / PR 模板，不放 AGENTS.md）

agent 文档管「怎么写代码」；AI 提交政策管「怎么交 PR」，分开放：

- **人类责任不可转移**（共识）：AI 辅助不免除提交者理解与验证的责任。
- **披露可选，核验必须**：Kazumi 强制披露模型名 + PR 描述人工填写；folia 要求本地人工核验所有审查结果，不强制披露。
- **拒绝 slop 与修复循环**：「AI 生成→修复→修复→修复」的循环不收（Kazumi）；未经审阅的生成不收。

---

## 8. 模板骨架（按项目填充，不是固定答案）

```markdown
# AGENTS.md — {项目名}

> coding agent 的项目约定。活文档，随项目演进。CLAUDE.md 指向本文件。

## 项目概览
{一句话} · 栈：{TECH-STACK 选定} · 设计系统：{UI-DESIGN 选定或无}

## 架构地图
{repo layout + 依赖方向规则}

## 命令
- 安装 / 开发 / 测试 / lint / 验证：{exact，注明陷阱}

## 硬规则（Do / Don't）
- {项目特有禁区，逐条}

## 产出物语言
- 默认英文：README、仓库描述与 topics、项目文档、commit message、PR/Issue 标题与正文
- 仅当用户明确指定其他语言时切换，且只对该次指令生效；本套元文档的中文写作语言不构成产出语言依据
- {项目例外：如面向中文用户的 i18n 翻译件}

## 架构边界（机器检查）
- {依赖方向规则 + 对应 gate 命令}

## 变更食谱
### {高频操作}
{标准步骤，易错链路写明}

## 工作流与 Git 安全
- 不主动 commit/push/PR/开 Issue，除非用户明确要求交付（deliver / ship / push / 开 PR 同等含义）
- 只暂存明确路径，不用 git add . / -A；保留无关改动；main 不 force-push
- 用户明确覆盖默认规则（跳过 Issue / 直推 main / 忽略红 CI）仅当轮有效，且必须在 PR/Issue 评论中记录该覆盖

## 交付流程（Issue → PR → main → CI → merge）
规范闭环：
Issue open → PR open（Fixes #N，base=main）→ CI
  ├─ 红 → 修复再推（Issue 保持 open）
  └─ 绿 → 合并进 main → Issue 自动关闭

硬规则（逐条可判定）：
- PR 一律以 main 为 base，除非用户或维护者明确指定其他分支
- 有意的代码/文档变更 Issue 先行：已有跟踪该工作的 open Issue 就复用，没有才新建（标题短而可执行；正文 = 问题/目标 + 范围 + 验收标准）
- 分支从最新 main 切出；commit 只含目标文件，message 写清为什么
- PR 正文必须含 `Fixes #N` 或 `Closes #N` + 改了什么/为什么 + 测试说明；一个 PR 尽量只对应一个主 Issue，其余 Issue 只链接、不加关闭关键字
- Issue 只在合并后关闭：PR 刚打开不关、CI 红不关、未合并不关；CI 是合并门禁，required checks 全绿才合并，CI 本身不得自动关 Issue
- required check 名称写仓库里真实存在的 workflow + job id：{列出实际 job id}，不编造
- 提交不含 secrets 与机器本地垃圾（local.properties / keystore / IDE 缓存 / 凭据）
- 开 PR 后在 Issue 评论贴 PR 链接 + 一行状态（等 CI / 待维护者合并）
- 无合并权限时交接不越权：照常开 PR + Issue 评论留链接，Issue 保持 open，请维护者在绿灯后合并
- 收尾报告：分支、Issue URL、PR URL、CI 状态（红则附 job 链接）、merge SHA 或「等待维护者」

反模式：PR 打开即关 Issue；base 不是 main 且无明确覆盖；CI 红/缺失就宣称完成；CI 成功后自动关 Issue；对缺 `Fixes` 的 bot PR 一律硬失败（已有豁免的写明豁免）；常规功能直推 main。

配套按仓库需要落地。README 的贡献段给读者入口，较长的规则沿用现有贡献指南。在 `.github/pull_request_template.md` 提醒实际提交要求并链接规则。CI 和发布工作流按仓库实际设置维护。

## 安全 / 隐私
- 不 log 凭据；secrets 不进仓；{隔离设置}

## 验证
- {risk-matched 执行证明；green CI ≠ 真机}

## 技能（大项目）
- {skills/<name>/SKILL.md 索引，按需加载}
```

---

## 9. 反模式

| 反模式 | 后果 |
|---|---|
| 写通用百科（模型已知） | 烧 token，零收益 |
| stale 信息不更新 | 比没有更糟，误导 agent |
| 散文规则无 gate | 规矩不被执行 |
| 复制权威文档 | 漂移；应链接 |
| secrets 进文件 | 安全事故 |
| 过长无路由 | 关键规则被淹没 |
| 当成固定模板一次写完 | 失去活文档价值 |
| 多份指令不同步 | CLAUDE/AGENTS 漂移 |

---

> 时效与来源：截至 2026-11-16，实证抓取自 web-to-app / read-aware / folia-major / dsh-Go / BiliDesk / Kazumi 的 AGENTS.md / CLAUDE.md / CONTRIBUTING / PR 模板，及 GoogleChrome/modern-web-guidance-src 的 AGENTS.md。Kazumi 的文件位置另按[仓库指南中的快照](APP-REPOSITORY.md)复核。
