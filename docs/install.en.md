# Installation and updates

[简体中文](install.md)

## Supported Agents

Doubao, WorkBuddy, Claude Code, Codex, and other Agents that support Skills. In a Skills-enabled environment, use the command below or ask your Agent to install the collection.

## Quick installation

Run in a terminal with Node.js and `npx` available:

```bash
npx -y skills add ZanePan2027/zane-life-workbench -g --all
```

Select your Agent in the installer and reload Skills if the host requires it. Omit `-g` to install only in the current project.

Or ask your Agent:

```text
Install all Skills from https://github.com/ZanePan2027/zane-life-workbench.
Then use zane-workbench to help me with this: ...
```

## Start using it

Open the folder you want to keep using in your Agent and ask `zane-workbench` to connect or create your life workspace there. Existing rules and material are reused; an empty folder also works. If no location is chosen, the Agent helps you choose one once. Add relevant files without sorting them first, then start your current task. One-off questions do not require setup. Follow the [walkthrough](guide.en.md).

## Update and save work

Ask your Agent to compare the installed files with this repository and preserve your local edits before updating. Check the actual revision and content, even when the version number is unchanged.

The Skill directory holds methods. Your workspace holds personal material and results. Continue in the same project without repeating the folder path. A location is needed again only when the project changes, access is lost, or the workspace is ambiguous. When changing tools, open or authorize access to that same folder.

[Back to the overview](../README.en.md)
