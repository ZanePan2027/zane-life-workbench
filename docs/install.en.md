# Installation and updates

[简体中文](install.md)

## Supported Agents

Doubao desktop with local Skills, WorkBuddy, Claude Code, Codex, and other Agents that support Skills. Choose the installation method for your client below.

## Quick installation

For Agents listed in the installer, such as Codex and Claude Code, run in a terminal with Node.js and `npx` available:

```bash
npx -y skills add ZanePan2027/zane-life-workbench -g --skill "*"
```

`--skill "*"` selects all Skills. Select a target Agent in the installer and reload Skills if the client requires it. Omit `-g` to install only in the current project.

Or ask your Agent:

```text
Install all Skills from https://github.com/ZanePan2027/zane-life-workbench.
Then use zane-workbench to help me with this: ...
```

## Doubao and WorkBuddy

Send the installation request above in your client and tell the Agent which client you use.

| Client | Installation and discovery |
| --- | --- |
| WorkBuddy | Ask the Agent to install each folder under the repository's `skills/` into `.workbuddy/skills/` in your user home directory, including all files within it. Open the Skills page, go to your installed skills, find `zane-workbench`, and enable it. |
| Doubao for macOS with local Skills | Ask the Agent to install each Skill folder into `~/.agents/skills/`, then reload in the client's local Skills mode. |

If these clients are absent from the installer's list, use the method above. The entry should be `<skills-directory>/zane-workbench/SKILL.md`, without an extra repository folder in between. Start a new conversation and ask: “Use zane-workbench to help me with …”.

## Start using it

Open the folder you want to keep using in your Agent and ask `zane-workbench` to connect or create your life workspace there. Existing rules and material are reused; an empty folder also works. If no location is chosen, the Agent helps you choose one once. Add relevant files without sorting them first, then start your current task. One-off questions do not require setup. Follow the [walkthrough](guide.en.md).

## Update and save work

Ask your Agent to compare the installed files with this repository and preserve your local edits before updating. Check the actual revision and content, even when the version number is unchanged.

The Skill directory holds methods. Your workspace holds personal material and results. Continue in the same project without repeating the folder path. A location is needed again only when the project changes, access is lost, or the workspace is ambiguous. When changing tools, open or authorize access to that same folder.

[Back to the overview](../README.en.md)
