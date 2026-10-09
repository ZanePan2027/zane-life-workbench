# Beyond the Ivory Tower

[简体中文](README.md) | English

> Get help with the job-search problem in front of you—from choosing roles to applications, interviews and offers.

[![Version](https://img.shields.io/badge/version-v1.0.0-2563EB.svg?style=flat-square)](VERSION.md)
[![License](https://img.shields.io/badge/license-MIT-16A34A.svg?style=flat-square)](../../LICENSE)

**An AI toolkit for the steps before starting a job, primarily for interns, new graduates and people with 1–2 years of experience.** Experienced applicants can use it too; their actual responsibilities and seniority are preserved.

**Supports Doubao, WorkBuddy, Claude Code, Codex, and other Agents that support Skills.**

[Quick start](#quick-start) · [Tasks](#tasks) · [Guide](guide.en.md) · [Skills](skill-inventory.en.md) · [Installation](install.en.md)

![Start with your current job-search task](career-assets-flow.en.svg)

Bring an old résumé, a job description, project material, an interview question or an offer. Ask for the result you need. Start with the task that matters to you now.

## Quick start

```bash
npx -y skills add ZanePan2027/zpskill -g --skill zane-career-application-greeting zane-career-assets zane-career-case-editor-zh zane-career-portfolio-architecture zane-career-portfolio-builder zane-career-portfolio-website-design zane-career-resume-builder zane-design-reference-to-prompt zane-evidence-weighted-case-storytelling zane-former-employer-data-redactor zane-portfolio-multi-format-qa
```

Or tell your Agent:

```text
Install the Career Skills (11: zane-career-application-greeting, zane-career-assets, zane-career-case-editor-zh, zane-career-portfolio-architecture, zane-career-portfolio-builder, zane-career-portfolio-website-design, zane-career-resume-builder, zane-design-reference-to-prompt, zane-evidence-weighted-case-storytelling, zane-former-employer-data-redactor, zane-portfolio-multi-format-qa) from https://github.com/ZanePan2027/zpskill.
Then use zane-career-assets to help me with this task: …
```

The command works with Agents listed in the installer, including Codex and Claude Code, and requires Node.js and `npx`. For Doubao or WorkBuddy, use the Agent request above and follow the [host-specific instructions](install.en.md).

```text
Use zane-career-assets. Here are my old résumé and the role I want.
I mainly apply through BOSS Zhipin. Rework my résumé, write the opening
of my online profile, and draft a first message for this role.
Make an editable version first; I'll give feedback on it.
```

The Agent uses what you have provided and asks only about gaps that affect the result. It normally completes a candidate and checks it. If you prefer to approve the text before design, say so.

## Tasks

| Need | Result |
| --- | --- |
| Choose roles or find experience without internships | Role comparisons, honest material from school and projects, practical next steps |
| Find internships or interpret a job description | Search criteria, verifiable openings when access is available, eligibility and fit |
| Improve BOSS Zhipin profile and messages | Profile opening, supporting strengths, role-specific greeting and follow-up |
| Rebuild or localize a résumé | Content, layout and requested editable or export files |
| Create a portfolio | Work selection, case studies, documents or a website as needed |
| Prepare for tests and interviews | Practice, answer editing and one-question-at-a-time mock interviews |
| Compare offers and negotiate | Comparable compensation, questions to resolve and reply drafts |
| Prepare for signing and starting | Relevant document checks, questions and timing |

## Designed for recruitment platforms

An online profile opening establishes relevance. The full profile and attachment provide evidence. A greeting connects it to this role; a portfolio provides depth when useful. These touchpoints share facts but serve different purposes.

The observed recruiter recommendation list shows about 22 Chinese characters of the profile opening. Aim to convey one relevant strength within 20–22 characters, then expand it for search results and the full profile. The Agent adapts the copy to your interface. [Interface observations](../../skills/zane-career-assets/references/platform-evidence.md)

## Continue when useful

A one-off task can finish immediately. For ongoing work, save the current version and pause point in your existing project. Continue there without repeating a known folder path. In chat-only tools, keep a short handoff summary.

The toolkit contains 11 Skills. Start with `zane-career-assets`, or select a [specialist](skill-inventory.en.md).

See the [guide](guide.en.md), [validation scope](testing.md) and [design sources](provenance.md). Share your experience through Issues, with personal and company details removed.

[MIT License](../../LICENSE). Author: Zane.
