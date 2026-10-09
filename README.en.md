# zpskill

[简体中文](README.md) | English

> Zane's Life-Management Skills: help you run your own life well, and live it without letting yourself down.

[![Version](https://img.shields.io/badge/version-1.0.0-2563EB.svg?style=flat-square)](VERSION.md)
[![License](https://img.shields.io/badge/license-MIT-16A34A.svg?style=flat-square)](LICENSE)

**Works with Doubao, WorkBuddy, Claude Code, Codex, and other Agents that support Skills.**

zpskill is created by [Zane](https://github.com/ZanePan2027) and does one thing: help people run their own lives well. It holds 18 Skills today: the main line, Live Your Life Well (7), and one concrete thing in a life, finding a job (11).

[Quick start](#quick-start) · [Install](#install) · [What's inside](#whats-inside) · [How it works](#how-zpskill-works) · [Manuals](#manuals) · [Changelog](CHANGELOG.md)

![How your life adviser works](docs/life/life-flow.en.svg)

---

## What zpskill solves

It does not help you live the most cost-efficient life. It helps you live the life you find worth living. An afternoon asleep in the sun with nothing to show for it can be a day worth having. So it first learns, in your own words, what life you want, what energizes you, and where your limits are, then helps you get the things you want done.

| What you bring | What you get |
|---|---|
| A good job is drifting away from the life you want | A decision grounded in your goals, a transition route, and practical arrangements |
| Someone praises you but keeps expanding the work | An assessment of incentives and behavior, negotiation material, and alternatives |
| Circumstances are changing quickly | Main possible directions, timing, preparation, and signals to change course |
| Work, care, and personal projects compete for attention | A feasible overall plan and commitments to renegotiate |
| You feel stuck before starting something | The sticking point understood first, then one step you actually want to take, made doable |
| You feel overwhelmed and want to be understood | Listening, shared understanding, and support at your pace |
| You keep repeating the same background | Saved understanding, usable outputs, and a clear place to resume |
| You do not know what to apply for, or how to write a résumé with no internship | Role comparisons, honest material from school and projects, small projects to try |
| BOSS Zhipin: what to write, and why greetings get no reply | Profile opening, supporting strengths, role-specific greeting and follow-up |
| An old résumé to rebuild, an English version, or a portfolio with few projects | Résumé and portfolio content, layout and the files you need for the role and market |
| You do not know how to prepare for tests and interviews | Practice, answer editing and one-question-at-a-time mock interviews |
| How to compare offers, negotiate and reply | Comparable compensation, questions to resolve and reply drafts |

---

## Quick start

Remember one entry: `zp-life`. After installing, tell your Agent:

```text
Use zp-life.
My job pays steadily, but last-minute requests fill every day.
Over the next six months I want more time for family and my own writing.
Help me understand how this could develop and what to do now.
```

You get a recommendation and the reasoning that matters, followed by the comparisons, arrangements, or message drafts you need. Continue with new facts, such as “They agreed, but haven't assigned a replacement yet,” and it revises the same plan. You can also start with: `I am tired today. Stay with me for a while; I do not need advice yet.`

When you already know what you need, call a specific Skill:

```text
Use zp-career. Here are my old résumé and the role I want. I mainly apply through BOSS Zhipin. Rework my résumé, write the opening of my online profile, and draft a first message for this role.
Use zp-resume to make an English résumé for a product internship from these experiences.
Use zp-self: why do I give up just when I am about to succeed?
Use zp-workspace to set this folder up as my life workspace, then help me with: …
```

To have it remember you over time, open a folder you plan to keep using and ask it to set up a life workspace; next time say “Continue from last time”. It works without a workspace too. You do not need to learn a method or organize files first.

---

## Install

Run in a terminal; Node.js and `npx` required.

### Recommended: everything

```bash
npx -y skills add ZanePan2027/zpskill -g --all
```

Then tell your Agent “Use zp-life, help me…”.

To install only part:

**Main line: Live Your Life Well (7)**

```bash
npx -y skills add ZanePan2027/zpskill -g --skill zp-life zp-workspace zp-question zp-partner zp-self zp-support zp-guide
```

**Job search: finding a job (11)**

```bash
npx -y skills add ZanePan2027/zpskill -g --skill zp-greeting zp-career zp-editor zp-portfolio zp-materials zp-site zp-resume zp-design-prompt zp-story zp-redact zp-qa
```

### Claude Code plugin marketplace

```bash
claude plugin marketplace add ZanePan2027/zpskill
claude plugin install zpskill@zpskill
```

With the full set, Skills appear in chat prefixed with `zpskill:`, for example `zpskill:zp-life`. You can also install one Skill, for example `claude plugin install zp-career@zpskill`, which shows as `zp-career`. Just say “Use zp-life, help me…”; the full name is not required.

### Without the command line (Doubao, WorkBuddy, etc.)

Tell your Agent “Install all Skills of zpskill from https://github.com/ZanePan2027/zpskill”, then start a new chat and say “Use zp-life, help me…”. Host-specific steps: [Life install](docs/life/install.en.md) · [Career install](docs/career/install.en.md).

### Update

If already installed, run the install command again, or tell your Agent:

```text
Use zp-life to update zpskill
```

Your own life workspace and files are untouched; only the Skills are replaced. See the [changelog](CHANGELOG.md).

---

## What's inside

### Main line: Live Your Life Well

Day to day you only need `zp-life`; the rest are used as the question requires.

| Entry | What you get |
|---|---|
| `zp-life` | Life strategy and foresight: a route, timing and practical setting, usable outputs, next steps |
| `zp-question` | A vague question turned into what you actually want to move forward |
| `zp-self` | Motives, values and recurring choices understood from real experience |
| `zp-support` | Emotional and psychological support; not a substitute for diagnosis or treatment |
| `zp-partner` | Responsibilities, judgment and collaboration for a long-term AI partner |
| `zp-workspace` | Build a workspace, organize sources, resume where you stopped |
| `zp-guide` | When you need concrete everyday options, consults the [How To Live Better guide](https://github.com/eternity4719/HowToLiveBetter) with sources |

### A concrete thing: finding a job

![Start with your current job-search task](docs/career/career-assets-flow.en.svg)

Finding a job is one concrete thing in a life. This AI job-search toolkit walks with you through every step before you start work, mainly for interns, new graduates and people with 1–2 years of experience; experienced people changing jobs can use it too. Day to day you only need `zp-career`; it reads the methods the task needs and completes it. Call a specific tool directly once you know it.

| Entry | What you get |
|---|---|
| `zp-career` | Single entry: direction, openings, platform messages, materials, interviews, offers, negotiation, pre-start prep |
| `zp-materials` | Résumé, portfolio and application entry points planned and made together |
| `zp-resume` | A résumé from scratch, or rewritten for a hiring market and language |
| `zp-greeting` | First message and follow-ups on BOSS Zhipin and similar platforms |
| `zp-portfolio` | Layered portfolio structure and bilingual application entry |
| `zp-site` | A personal portfolio site: reading path, visual design, responsive pages |
| `zp-editor` | Chinese case studies and long-form job-search writing edited to read like a person, keeping judgment and trade-offs |
| `zp-story` | Project stories told in proportion to the evidence, without overstating |
| `zp-qa` | Pre-publish checks across web, Word/PDF, links and numbers |
| `zp-redact` | Redact former-employer data and sensitive details before they go in a portfolio |
| `zp-design-prompt` | Turn design references into reusable generation prompts |

Later workspaces and tools will live here too, not in separate projects.

---

## How zpskill works

```text
The life you want
   ↓
Current stage · people and circumstances
   ↓
Possible futures
   ↓
Routes · timing · practical setting
   ↓
Get the thing in front of you done (finding a job, for example)
   ↓
Adjust with what really happens
```

zpskill handles one current thing at a time. For an important decision it keeps your view, the AI's advice, each side's basis and the signals that would change the judgment; when reality comes back, it fixes the current plan first, then asks which understanding is worth keeping.

---

## Manuals

How to use it well once installed: [Live Your Life Well (main line)](docs/life/README.en.md) · [Finding a job](docs/career/README.en.md)

---

## Author and support

By [@ZanePan027](https://x.com/zanepan027) · [Xiaohongshu](https://xhslink.cn/o/7CiaOyzr6UO) · [Douyin](https://v.douyin.com/k3MsOVPRIKY)

To join the community, scan the code or open the [community guide (in Chinese)](https://mp.weixin.qq.com/s/w0TrK3N4XDiOSdrQ-iB0vQ).

![Community QR code](docs/join-community.png)

## License

This project uses the [MIT](LICENSE) license.

- Personal, learning, research and commercial use are all allowed.
- Keep the copyright and license notice when you copy or redistribute it.
- The software is provided "as is", without warranty of any kind.
