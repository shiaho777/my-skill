---
name: upstream-sync
description: >
  将本地 Git 分支或 fork 同步到真正的上游，支持同步上游、pull upstream、
  sync fork 和与上游默认分支对齐。先区分本地同步与推送 fork。
---

# Git 上游同步

## 确认同步的是哪条分支

检查工作区、当前分支、进行中的 merge/rebase、远端地址和上游真实默认分支。区分 fork 的 `origin`、源仓库远端、当前分支的跟踪分支。同步 fork 主线时定位本地主线，当前 feature 分支保留给自己的任务。上游可由现有配置或已核实的 fork 关系得出，无法确定时再询问。对于 ZIP 解压目录，另建干净克隆并列出差异，原目录留作参考。

更新已确认的上游跟踪引用，用 `git rev-list --left-right --count <local-target>...<upstream-ref>` 比较明确的本地和上游引用。动手前在检出的目标分支再次确认 `HEAD`。目标不在当前工作区时优先使用其已有的干净 worktree，或在未被检出的情况下另建 worktree。工作区有改动或已有 Git 操作时先保全现场，取得授权后再暂存或接手。

## 根据提交关系行动

| 分支情况 | 操作 |
|---|---|
| 上游已包含在本地 | 报告同步状态及仍在本地的提交。 |
| 仅落后 | 对已确认的目标分支执行 `git merge --ff-only <upstream-ref>`。 |
| 双方都有独有提交 | 列出本地独有提交并检查补丁等价。用 `git cherry <upstream-ref> <local-target>` 辅助判断，squash 等场景再核对实际 diff。报告历史可否改写与冲突风险，按用户选择执行 rebase、merge 或保留现状。 |

分叉开始合并或改写前记录旧 HEAD 并建立可恢复的备份引用。冲突时说明文件双方意图和具体取舍，按已有授权解决，其余留给用户决定。在继续 Git 操作前检查冲突 diff，重跑会受影响的验证。[Git 合并](https://git-scm.com/docs/git-merge) · [补丁等价](https://git-scm.com/docs/git-cherry)

## 确认完成

核对上游提交已被目标分支包含，报告分支、前后 SHA、工作区状态与备份位置。单独确认推送 fork 的授权以及远端目标。正常推送遇到非快进时先核对原因。只有用户明确允许改写该远端分支时才可使用 `--force-with-lease=<远端分支引用>:<已核验的原远端SHA>`，远端发生并发变化则停在安全状态。[Git 推送](https://git-scm.com/docs/git-push)
