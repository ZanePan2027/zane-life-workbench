# zpskill｜Zane的人生经营Skills

简体中文 | [English](README.en.md)

> Zane的人生经营Skills：一套陪你把人生想清楚，一套陪你把工作找到。免费开源。

**支持：豆包、WorkBuddy、Claude Code、Codex，以及其他支持 Skills 的 Agent。**

## 你想先解决哪件事

| 我想…… | 用这一套 | 内容 |
|---|---|---|
| 看清自己想过什么样的人生，处理选择、关系、转折，长期有人接着陪 | [过好你的人生](docs/life/README.md) | 7 个 Skill，入口 `zane-workbench` |
| 找实习或工作：简历、作品集、投递、面试、offer | [走出象牙塔](docs/career/README.md) | 11 个 Skill，入口 `zane-career-assets` |

两套彼此独立，可以只装其中一套。

## 安装

只装「过好你的人生」：

```bash
npx -y skills add ZanePan2027/zpskill -g --skill zane-workbench zane-workbench-curator zane-question-intent-translator zane-agent-identity-card-builder zane-self-insight zane-psychological-support life-decision-guide
```

只装「走出象牙塔」：

```bash
npx -y skills add ZanePan2027/zpskill -g --skill zane-career-application-greeting zane-career-assets zane-career-case-editor-zh zane-career-portfolio-architecture zane-career-portfolio-builder zane-career-portfolio-website-design zane-career-resume-builder zane-design-reference-to-prompt zane-evidence-weighted-case-storytelling zane-former-employer-data-redactor zane-portfolio-multi-format-qa
```

两套都装：

```bash
npx -y skills add ZanePan2027/zpskill -g --all
```

Claude Code 插件市场：

```bash
claude plugin marketplace add ZanePan2027/zpskill
claude plugin install zpskill@zpskill
```

也可以只装单个 Skill，例如 `claude plugin install zane-career-assets@zpskill`。

安装后新建对话，说“使用 zane-workbench，帮我……”或“使用 zane-career-assets，帮我……”即可。具体入口见各自的安装与更新页：[人生](docs/life/install.md) · [求职](docs/career/install.md)。

## 关于仓库

本仓库由原来的 zane-life-workbench 和 zane-career-skills 合并而来，旧地址会自动跳转，原有的提交历史保留在这里。

欢迎在 [Issues](https://github.com/ZanePan2027/zpskill/issues) 分享你想完成的事、实际过程和希望改善的地方。公开分享前请自行去除个人与公司敏感信息。[参与贡献](CONTRIBUTING.md) · [许可证](LICENSE)（MIT）
