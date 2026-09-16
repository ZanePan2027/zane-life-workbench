# Live Your Life Well

[简体中文](README.md) | English

> Turn your current situation into choices you can stand behind and actions you can follow through on.

[![Version](https://img.shields.io/badge/version-v1.0.0-2563EB.svg?style=flat-square)](VERSION.md)
[![License](https://img.shields.io/badge/license-MIT-16A34A.svg?style=flat-square)](LICENSE)

An AI life workbench that starts with what is happening now. Understand your situation, weigh choices, coordinate time and responsibilities, complete useful work, and adjust as life changes. You decide what living well means.

**For Claude Code, Codex, and other tools that support Agent Skills. Free and open source.**

[Quick start](#quick-start) · [What it helps with](#what-it-helps-with) · [Guide](docs/guide.en.md) · [Skill directory](docs/skill-inventory.en.md) · [Installation and updates](docs/install.en.md)

![From a current question to continued progress](docs/life-flow.en.svg)

**Start with `zane-workbench` and describe the task at hand.** It selects the methods needed for your task. You can begin with the material you already have.

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

### 2. Describe the task

```text
Use zane-workbench.
I am comparing two jobs: one pays more but has a longer commute;
the other offers more flexibility. I care about financial stability
and time with my family. Here are the offers and my monthly expenses.
Help me compare workable arrangements and the tradeoffs of each.
```

A useful first result is a comparison of time, spending, conditions still to confirm, and possible next steps. The Agent asks for missing information when it affects the judgment.

### 3. Bring back changes

```text
The first employer has now confirmed two remote days per week. Revisit the comparison.
Save the result and outstanding questions in my workspace so I can continue later.
```

An undecided choice stays recorded as undecided. You can continue by asking for a document, a schedule, or a revised budget.

## What it helps with

| What you can say | What you can get |
| --- | --- |
| Both jobs have advantages. Which fits my life now? | A comparison using your priorities, finances, time, and responsibilities |
| Can work, family time, and study fit into this week? | A weekly plan, conflicts, and arrangements to change or discuss |
| I want to move. Where do I start? | Preparation and next steps based on your conditions |
| I keep returning to the same choices. What matters to me? | Tentative insights grounded in experience, with practical things to try |
| The conditions changed. How do I continue? | Revised judgments, work, and a saved stopping point |

## Save and continue

Give the Agent the workspace folder you want to use. In a later session, provide that location and ask it to continue the job comparison. It reads the saved material to recover the current judgment and next step.

In ordinary chat, save a continuation note and paste it back with the relevant material. Naming the product alone does not load the complete Skill. See [starting in chat](docs/chat-start.en.md).

[Follow a job comparison](docs/guide.en.md)

## Use a specific method

Continue using `zane-workbench` for everyday tasks. Once familiar, you can directly select question clarification, self-reflection, AI partner setup, or workspace organization. The [Skill directory](docs/skill-inventory.en.md) includes situations, example requests, and outputs.

## Choosing between the two toolkits

Start here when weighing work, family, finances, and personal direction together. For matching experience to roles, creating resumes and portfolios, or practicing interviews, use [Beyond the Ivory Tower](https://github.com/ZanePan2027/zane-career-skills). Each toolkit works independently.

## Current revision and validation

The product remains **1.0** (component metadata: **1.0.0**), revised **2026-09-16**. Internal iterations do not increase the version before external acceptance. Revision dates and commits identify the exact content.

Start with one question and the material you already have. Internal tests produced a working workspace from loose files, a useful comparison, revisions after new feedback, and continuation in a fresh session. External user acceptance is still pending. Models may skip parts of long source material, so complete and reliable judgments are not guaranteed. See [validation and known limitations](docs/testing.md).

The distribution contains general methods, tools, and templates. It does not contain the author's private records, conversations, finances, or real-life task data, or prefill the author's personal goals. Your AI works with material you supply or authorize it to read; data handling depends on your AI tool and settings.

## Provenance and license

The collection grew from question clarification, AI partner design, and self-reflection into a workflow for choices, action, feedback, and continuity.

See [Provenance](docs/provenance.md) for design references. This repository is released under the [MIT License](LICENSE).

Author: Zane
