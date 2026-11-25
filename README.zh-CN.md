# My Skill

[English](README.md)

这里收录我平时放在 `~/.agents/skills` 里用的一些 Skill。你可以直接读里面的说明，看看我怎么把常见开发任务交给 AI，也可以挑有用的装到自己的工具里。

| Skill | 适用场景 | 可以这样问 |
|---|---|---|
| [issue-pr-ci-delivery](skills/issue-pr-ci-delivery/SKILL.md) | 在 GitHub 上提交、推送或跟进 PR，做到你要求的阶段。 | 「只提交目前暂存的改动，提交留在本地。」 |
| [md-docs-beautify](skills/md-docs-beautify/SKILL.md) | 改善 Markdown 文档，用仓库里的实际信息配图。 | 「快速开始下面加一张架构图，也同步到中文版 README。」 |
| [open-source-product-playbook](skills/open-source-product-playbook/SKILL.md) | 验证开源产品选题，选择技术栈和界面方向，准备首次发布。 | 「帮我判断这个开源应用想法值不值得做，首版需要做到什么程度？」 |
| [repo-maintenance](skills/repo-maintenance/SKILL.md) | 找值得做的开源贡献、检查 PR、处理评审和 CI。 | 「帮我检查这个 PR 能不能发，列出还有哪些地方卡着。」 |
| [upstream-sync](skills/upstream-sync/SKILL.md) | 把 Git 仓库或 fork 的指定分支和上游对齐。 | 「把 fork 的默认分支同步到上游，保留我现在的功能分支。」 |

## 安装单个 Skill

先克隆仓库，再复制整个 Skill 目录。这样引用的资料和脚本也会一起安装。以 `repo-maintenance` 为例：

```sh
git clone https://github.com/shiaho777/my-skill.git
cd my-skill
my_skill_target="$HOME/.agents/skills/repo-maintenance"
if [ -e "$my_skill_target" ] || [ -L "$my_skill_target" ]; then
  printf 'Skill already exists at %s\n' "$my_skill_target"
else
  mkdir -p "$HOME/.agents/skills" && cp -R skills/repo-maintenance "$my_skill_target"
fi
```

安装其他 Skill 时，把命令里两处 `repo-maintenance` 都换成对应名称。如果你的工具用别的用户 Skill 目录，改一下目标路径即可。[Agent Skills 格式](https://agentskills.io/specification)

## 维护

每个 Skill 在 [`skills/`](skills/) 下有单独目录。维护时把 `SKILL.md` 引用的资料和脚本放在同一目录树里。更新本地副本前，先看看仓库里的改动，尤其是你在本地做过修改时。

遇到说明看不懂或步骤失效，欢迎提 Issue。写上 Skill 名称、你想完成的任务，以及实际发生了什么。
