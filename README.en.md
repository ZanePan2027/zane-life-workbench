# zpskill｜Zane's Life-Management Skills

[简体中文](README.md) | English

> Two free, open-source sets of AI Skills: one helps you work out the life you want, the other helps you find the job.

**Works with Doubao, WorkBuddy, Claude Code, Codex, and other Agents that support Skills.**

## Which one do you need

| I want to… | Use | Contents |
|---|---|---|
| Understand what life I want to live, handle choices, relationships and turning points, with something that keeps going over time | [Live a Life Worth Living](docs/life/README.en.md) | 7 Skills, entry `zane-workbench` |
| Find an internship or job: resume, portfolio, applications, interviews, offers | [Out of the Ivory Tower](docs/career/README.en.md) | 11 Skills, entry `zane-career-assets` |

The two sets are independent; install either one or both.

## Install

Life only:

```bash
npx -y skills add ZanePan2027/zpskill -g --skill zane-workbench zane-workbench-curator zane-question-intent-translator zane-agent-identity-card-builder zane-self-insight zane-psychological-support life-decision-guide
```

Career only:

```bash
npx -y skills add ZanePan2027/zpskill -g --skill zane-career-application-greeting zane-career-assets zane-career-case-editor-zh zane-career-portfolio-architecture zane-career-portfolio-builder zane-career-portfolio-website-design zane-career-resume-builder zane-design-reference-to-prompt zane-evidence-weighted-case-storytelling zane-former-employer-data-redactor zane-portfolio-multi-format-qa
```

Both:

```bash
npx -y skills add ZanePan2027/zpskill -g --all
```

Claude Code plugin marketplace:

```bash
claude plugin marketplace add ZanePan2027/zpskill
claude plugin install zpskill@zpskill
```

A single Skill also works, for example `claude plugin install zane-career-assets@zpskill`.

After installing, start a new chat and say "Use zane-workbench to help me…" or "Use zane-career-assets to help me…". Details: [Life install](docs/life/install.en.md) · [Career install](docs/career/install.en.md).

## About this repository

This repository merges the former zane-life-workbench and zane-career-skills. Old URLs redirect here and the commit history is kept.

Share your task, experience, and suggested improvements in [Issues](https://github.com/ZanePan2027/zpskill/issues). [Contributing](CONTRIBUTING.md) · [License](LICENSE) (MIT)
