# Installation and updates

[简体中文](install.md)

## Supported Agents

Doubao, WorkBuddy, Claude Code, Codex, and other Agents that support Skills. Choose the installation method for your client below.

## Quick installation

For Agents listed in the installer, such as Codex and Claude Code, run in a terminal with Node.js and `npx` available:

```bash
npx -y skills add ZanePan2027/zpskill -g --skill zp-greeting zp-career zp-editor zp-portfolio zp-materials zp-site zp-resume zp-design-prompt zp-story zp-redact zp-qa
```

`--all` installs all Skills into every Agent the installer supports, with no prompts; reload Skills if the client requires it. To install into one Agent only, use `--skill "*" --agent <name>` instead. Omit `-g` to install only in the current project.

Or ask your Agent:

```text
Install the Career Skills (11: zp-greeting, zp-career, zp-editor, zp-portfolio, zp-materials, zp-site, zp-resume, zp-design-prompt, zp-story, zp-redact, zp-qa) from https://github.com/ZanePan2027/zpskill.
Then use zp-career to help me with this: ...
```

## Doubao and WorkBuddy

Send the installation request above in your client and tell the Agent which client you use.

| Client | Installation and discovery |
| --- | --- |
| WorkBuddy | Ask the Agent to install each folder under the repository's `skills/` into `.workbuddy/skills/` in your user home directory, including all files within it. Open the Skills page, go to your installed skills, find `zp-career`, and enable it. |
| Doubao for macOS · local computer | Start a local-computer work task and ask the Agent to install each Skill folder into `~/.agents/skills/`. Find them under the local section of Skills management, then invoke them in a work task. |
| Doubao web · cloud computer | Open [Doubao web](https://www.doubao.com/chat/), select Work → Cloud computer, and send the installation request. Ask the Agent to identify the supported persistent cloud skill directory before installing. |

Doubao cloud and local computers have separate Skill installations. For persistent cloud Skills, use the platform's skill management mechanism or its `user_skills` directory; installations elsewhere in the temporary sandbox may be removed when it is cleared. Browser-based work tasks are described in Doubao's official [access guide](https://www.doubao.com/work/docs/zh-cn/articles/462191106451-access) and [work task guide](https://www.doubao.com/work/docs/zh-cn/articles/047323472965-work-task-mode).

If these clients are absent from the installer's list, use the method above. The entry should be `<skills-directory>/zp-career/SKILL.md`, without an extra repository folder in between. Start a new conversation and ask: “Use zp-career to help me with …”.

## Start using it

Use `zp-career` and describe your current task with the material you have. Follow the [walkthrough](guide.en.md) for an example.

## Update and save work

Ask your Agent to compare the installed files with this repository and preserve your local edits before updating. Check the actual revision and content, even when the version number is unchanged.

The Skill directory holds methods. Keep your own material and results in a separate project folder you choose. Provide that folder when continuing a task later.

[Back to the manual index](README.en.md)
