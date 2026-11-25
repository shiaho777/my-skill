---
name: issue-pr-ci-delivery
description: >
  交付 GitHub 仓库已有改动，或建立仓库级 Issue、PR 和 CI 交付流程。
  用于提交、推送、发 PR、跟进 CI、合并和配置交付规范。根据用户授权选择停止点。
---

# GitHub 交付

## 先确定交付到哪一步

| 用户意图 | 交付终点 |
|---|---|
| 提交、commit | 本地提交并报告 SHA。 |
| 推送、push | 发布已有的目标提交。 |
| 交付、ship | 提交目标改动并发布到约定远端。授权范围与仓库规则决定是否走 PR。 |
| 开 PR、跟到合并、合并此 PR | 开 PR 到创建或更新为止。跟到合并要处理本范围内的 CI 失败并验明结果。合并指定 PR 时以该 PR 为准。 |
| 建立交付流程 | 检查现状，按请求更新仓库规则、贡献指南、PR 模板或 CI 配置。 |

核对当前分支、工作区与暂存区、目标仓库、远端及仓库规则。用户指定已暂存内容时以暂存快照为准。存在其他已暂存改动时用隔离的临时 index 保全原暂存区，避免路径式提交带入同文件未暂存改动。推送前审查相对已核实远端目标的全部待发布提交和 diff，排除无关改动、秘密及机器本地文件。保护规则或非快进拒绝需要用仓库允许且已获授权的路径处理。

## PR 路径

1. 确认目标仓库、head 和 base。目标以用户指定或仓库约定为准，通常是仓库默认分支。每次创建前按目标仓库、base 和带 fork 所有者的 head 查重。按仓库规范复用已有 Issue，需要建 Issue 时核对任务授权。
2. 检查从 merge base 到 head 的完整 PR diff，用项目现有检查验证改动。按模板说明改动、用户可见结果和验证情况。PR 确实解决 Issue 且以默认分支为目标时，按约定写 `Fixes #N`，跨仓库写全仓库名。部分修复或其他 base 用普通引用。状态已经由 PR 表达时，只有仓库流程或用户要求才同步留言。[GitHub Issue 关联规则](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)
3. 合并前确认 PR 的当前 head、必需检查、审批和合并队列要求。跟进到用户要求的终点，能在本任务范围内修复的失败，修复后重新跑检查。需要维护者操作或权限不足时报告实际阻塞。按规则合并后验证合并结果和预期的 Issue 状态。[GitHub 分支保护](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)

## 建立流程

先核对已有 `AGENTS.md`、`CONTRIBUTING`、PR 模板、CI 的触发条件与真实 job 名称，再把工作分工写到合适的文件。模板只保留改动摘要、验证结果和适用的 Issue 引用。只有仓库实际设置的 checks 才称为必需，分支保护或队列设置按用户授权处理。需要可移植模板时，把 base、必需检查和合并职责留为按仓库填写的项。

交付报告给出提交 SHA、推送目的地或 PR 链接、实际运行的验证和最终状态。恢复已有操作时沿用已经完成的提交与 PR。
