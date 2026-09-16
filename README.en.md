# Live Your Life Well

[简体中文](README.md) | English

> Turn your current situation into choices you can stand behind and actions you can follow through on.

[![Version](https://img.shields.io/badge/version-v1.0.0-2563EB.svg?style=flat-square)](VERSION.md)
[![License](https://img.shields.io/badge/license-MIT-16A34A.svg?style=flat-square)](LICENSE)

An AI life workbench that starts with what is happening now. Understand your situation, weigh choices, coordinate time and responsibilities, complete useful work, and adjust as life changes. You decide what living well means.

**For Claude Code, Codex, and other tools that support Agent Skills. Free and open source.**

[Quick start](#quick-start) · [What it helps with](#what-it-helps-with) · [Guide](docs/guide.en.md) · [Skill directory](docs/skill-inventory.en.md) · [Installation and updates](docs/install.en.md)

![From a current question to continued progress](docs/life-flow.en.svg)

**Start with `zane-workbench`: connect or create your workspace, then work on one real task.** Add the relevant material you have. The Agent organizes access, reads what the task needs, and helps you use it. You can also begin without files.

<a id="install"></a>

## Quick start

### 1. Install

Run in your terminal:

```bash
npx -y skills add ZanePan2027/zane-life-workbench -g --all
```

Or ask your Agent:

```text
Install all Skills from https://github.com/ZanePan2027/zane-life-workbench.
Then use zane-workbench to help me with this: ...
```

Select your Agent in the installer, then reload Skills if required. The terminal command requires Node.js and `npx`. Omit `-g` to install for the current project; see the [installation guide](docs/install.en.md) for updates.

### 2. Connect or create your workspace

Open a project folder you want to keep using in your Agent, then say:

```text
Use zane-workbench. Set up my life workspace in the current folder.
Check the existing material and rules, create the entries I need,
and then help me with my current task.
```

An existing workspace is reused; an empty folder also works. If you have not chosen a location, say “This is my first time. Help me create a workspace.” The Agent helps you choose a location once.

### 3. Add material and start one task

Put relevant files in the workspace's material folder; new workspaces normally use `资料/`. You can also point the Agent to an existing authorized location. You do not need to sort everything or move your entire archive first.

```text
I am comparing two jobs. The offers and monthly expenses are in this workspace.
I care about financial stability and time with my family.
Find and read the relevant material, then compare workable arrangements
and the tradeoffs of each.
```

The Agent maintains navigation and source references, reads the relevant text, and creates a comparison, schedule, or other useful result. It asks for missing facts when they affect the judgment. With no files, describe your situation in the conversation; a complete life profile is not required.

### 4. Bring back changes and continue

```text
The first employer has confirmed two remote days per week.
Update the existing comparison and next step.
```

Workspace setup authorizes saving the task's relevant sources, results, and progress within its scope. Next time, open the same project and say “Continue the job comparison.” The Agent reads the current records without asking you to specify the folder again.

For a one-off question, edit, or conversation, you can start directly without setup.

## What it helps with

| What you can say | What you can get |
| --- | --- |
| Both jobs have advantages. Which fits my life now? | A comparison using your priorities, finances, time, and responsibilities |
| Can work, family time, and study fit into this week? | A weekly plan, conflicts, and arrangements to change or discuss |
| I want to move. Where do I start? | Preparation and next steps based on your conditions |
| I keep returning to the same choices. What matters to me? | Tentative insights grounded in experience, with practical things to try |
| The conditions changed. How do I continue? | Revised judgments, work, and a saved stopping point |

## Save and continue

Keep using the same workspace project. The Agent reads its records to recover the current judgment and next step. It asks for a location only when the project changes, access is lost, or several workspaces cannot be distinguished. When changing tools, open or authorize access to that same folder.

Adding a file does not mean it has been read. Ask the Agent to take in the new material, or ask a question that uses it; it reads and indexes the relevant content during that task. The workspace does not monitor files outside a session.

In ordinary chat, save a continuation note and paste it back with the relevant material. Naming the product alone does not load the complete Skill. See [starting in chat](docs/chat-start.en.md).

[Follow a job comparison](docs/guide.en.md)

## Use a specific method

Continue using `zane-workbench` for everyday tasks. Once familiar, you can directly select question clarification, self-reflection, AI partner setup, or workspace organization. The [Skill directory](docs/skill-inventory.en.md) includes situations, example requests, and outputs.

## Choosing between the two toolkits

Start here when weighing work, family, finances, and personal direction together. For matching experience to roles, creating resumes and portfolios, or practicing interviews, use [Beyond the Ivory Tower](https://github.com/ZanePan2027/zane-career-skills). Each toolkit works independently.

## Current revision and validation

The product remains **1.0** (component metadata: **1.0.0**), revised **2026-09-16**. Internal iterations do not increase the version before external acceptance. Revision dates and commits identify the exact content.

Connect a minimal workspace, then start with one question and the material you have. Earlier internal tests covered loose files, a comparison, feedback, and fresh-session continuation. Checks for this onboarding revision are recorded separately; historical tests do not validate the new behavior. External user acceptance is still pending. Models may skip parts of long source material, so complete and reliable judgments are not guaranteed. See [validation and known limitations](docs/testing.md).

The distribution contains general methods, tools, and templates. It does not contain the author's private records, conversations, finances, or real-life task data, or prefill the author's personal goals. Your AI works with material you supply or authorize it to read; data handling depends on your AI tool and settings.

## Provenance and license

The collection grew from question clarification, AI partner design, and self-reflection into a workflow for choices, action, feedback, and continuity.

See [Provenance](docs/provenance.md) for design references. This repository is released under the [MIT License](LICENSE).

Author: Zane
