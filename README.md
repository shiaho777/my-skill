# My Skill

[简体中文](README.zh-CN.md)

A collection of the personal agent skills I keep in `~/.agents/skills`. Read the files to see how I break down common development tasks, or install the skills you find useful.

| Skill | What it helps with | Example prompt |
|---|---|---|
| [issue-pr-ci-delivery](skills/issue-pr-ci-delivery/SKILL.md) | Commit, push, or follow a GitHub PR to the requested point. | “Commit just the staged changes. Keep the commit local.” |
| [open-source-product-playbook](skills/open-source-product-playbook/SKILL.md) | Research an open-source product idea, choose a stack and design direction, and prepare it for release. | “Help me evaluate this open-source app idea and figure out what the first release needs.” |
| [repo-maintenance](skills/repo-maintenance/SKILL.md) | Find work worth contributing, check PR readiness, or handle review and CI. | “Check whether my PR is ready to send and tell me what still blocks it.” |
| [upstream-sync](skills/upstream-sync/SKILL.md) | Sync the intended branch of a Git repository or fork with upstream. | “Sync the fork’s default branch with upstream. Keep my feature work where it is.” |

## Install one skill

Clone the repository, then copy the whole skill folder so its references and scripts stay with it. For example:

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

Replace `repo-maintenance` in both places to install a different skill. If your agent uses a different user skills directory, change the destination. [Agent Skills format](https://agentskills.io/specification)

## Maintenance

Each skill lives in its own folder under [`skills/`](skills/). Keep any linked references or helper scripts alongside `SKILL.md`. To update an installed copy, review the changes in the repository first, especially if you have local edits.

If an instruction is unclear or a step no longer works, open an issue with the skill name, the task you tried, and what happened.
