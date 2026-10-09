<div align="center">

# zpskill

**Zane的人生经营Skills**

一套陪你把人生想清楚，一套陪你把工作找到。

**支持：豆包、WorkBuddy、Claude Code、Codex，以及其他支持 Skills 的 Agent。**

[过好你的人生](#过好你的人生) · [走出象牙塔](#走出象牙塔) · [安装](#安装) · [English](README.en.md)

</div>

---

## 你想先解决哪件事

| 我想…… | 用这一套 | 入口 |
|---|---|---|
| 看清自己想过什么样的人生，处理选择、关系和转折，并且有人接着陪 | [过好你的人生](#过好你的人生)（7 个 Skill） | `zane-workbench` |
| 找实习或工作：简历、作品集、投递、面试、offer | [走出象牙塔](#走出象牙塔)（11 个 Skill） | `zane-career-assets` |

两套彼此独立，可以只装其中一套。装好后在 Agent 里说“使用 入口名，帮我……”就能开始，不需要先学一套方法，也不需要先整理资料。

---

## 过好你的人生

> 先认识你，再陪你过你觉得值得的人生。

它不帮你过性价比最高的人生，只帮你过你自己觉得值得的人生。一个下午晒着太阳睡一觉，没有任何产出，也可以是值得的一天。所以它先用你自己的话记住你想过怎样的生活、什么让你有劲、边界在哪里，再陪你把想做的事做成。

沿一条主线推进：**你想过的生活 → 当前阶段 → 人与局势 → 可能未来 → 路线与时间空间 → 做成眼前的事 → 根据反馈继续调整。**

![人生参谋怎样与你一起推进](docs/life/life-flow.zh-CN.svg)

### 你带来的事，和一起得到的帮助

| 你带来的事 | 一起得到的帮助 |
|---|---|
| 工作不错，却越来越不像自己想过的生活 | 从人生阶段和真正想保留的东西出发，比较过渡路线与下一步 |
| 对方说认可你，实际却不断加码 | 看清利益、行为和依赖，准备能用的沟通、边界和退路 |
| 局势在变，想知道接下来可能怎样 | 推演几种主要走向，找出时间窗口、提前准备和换路信号 |
| 工作、家人、身体和自己的事撞在一起 | 看整体容量，排出实际放得下的安排，减少互相挤压 |
| 想做一件事，却总在开始前停住 | 先理解卡点，再把真正愿意做的一步变成可执行的东西 |
| 最近很难受，只想先有人听 | 具体地听懂你正在经历什么；什么时候探索、练习或求助，由你决定 |
| 同一背景不想每次重讲 | 保存共同经历、当前路线和成果，让下一次更懂你 |

### 一句话就能开始

```text
使用 zane-workbench，做我的长期人生参谋。
我现在的工作收入还可以，但每天被临时任务占满。
我希望半年后能腾出时间照顾家人，也保留自己的创作。
请从我想过的生活出发，看看接下来可能怎样发展，现在怎么走。
```

它会先给出现在的建议和关键理由，再把需要的比较、安排、测算或沟通文字做出来。你接着说“对方同意了，但还没有安排接替的人”，它会据此更新原来的判断。想先被听一听也可以：“我今天很累，先陪我聊聊，不急着给建议。”

想让它长期记得你，在 Agent 里打开一个准备长期使用的文件夹，说“把当前文件夹设为我的人生工作台”，下次说“接着上次”就能从原来的判断和下一步继续。没有工作台也能用，临时问题和倾诉直接开始。

### 7 个 Skill

日常只需要 `zane-workbench`，其余按当前问题自动调用。

| Skill | 你会得到 |
|---|---|
| `zane-workbench` | 人生参谋、未来推演：推荐路线、时间空间、实际成果和下一步 |
| `zane-question-intent-translator` | 把模糊的问题理清成真正要推进的事 |
| `zane-self-insight` | 从具体经历理解自己的动机、价值和反复出现的选择 |
| `zane-psychological-support` | 情绪陪伴与心理支持，不替代诊断或治疗 |
| `zane-agent-identity-card-builder` | 设定长期 AI 伙伴的职责、判断方式和协作约定 |
| `zane-workbench-curator` | 建台、整理资料、接续上次停下的地方 |
| `life-decision-guide` | 需要具体生活办法时，按需参考《[高性价比人生指南](https://github.com/eternity4719/HowToLiveBetter)》并给出处 |

完整用法：[教程](docs/life/guide.md) · [工作台结构](docs/life/architecture.md) · [示例](docs/life/examples.md)

---

## 走出象牙塔

> 从不知道投什么，到写好材料、聊到面试、判断 offer。解决你眼前的求职问题。

面向入职前各环节的 AI 求职工具箱，重点服务实习生、应届毕业生和工作 1—2 年的新人，有经验、正在换工作的人也可以用。把旧简历、岗位截图、项目材料、面试问题或 offer 交给 Agent，说需要什么，从手头最急的一件事开始。

![从当前求职问题直接开始](docs/career/career-assets-flow.zh-CN.svg)

### 可以处理的事

| 当前问题 | 可以得到 |
|---|---|
| 不知道适合投什么，没有实习怎么写？ | 方向比较、真实经历取材与可尝试的小项目 |
| 到哪里找实习／校招／社招，怎样看 JD？ | 岗位筛选条件、可核查机会、资格与匹配判断 |
| BOSS 直聘开头写什么，打招呼总没回应？ | 在线简历首句、个人优势、岗位招呼语与沟通调整 |
| 旧简历要重做，想做英文版 | 针对岗位和市场的内容、版式及所需文件 |
| 需要作品集，但项目不多 | 可展示作品选择、案例内容、文档或网站 |
| 笔试、作业和面试不知道怎么准备 | 练习方案、回答改进、一问一答的模拟面试 |
| offer 怎么选，怎样谈薪或回复？ | 同口径待遇比较、待核实条款、谈薪与回复草稿 |
| 签约、背调、到岗前要准备什么？ | 针对当前情况的手续梳理、核实问题与时间安排 |

### 一句话就能开始

```text
请使用 zane-career-assets。这是我的旧简历和想投的岗位。
我主要用 BOSS 直聘，请帮我重做一份简历，
同时写好在线简历的个人优势开头和这个岗位的打招呼语。
先直接做出可编辑版本，我看完再提修改。
```

已有的信息直接使用，只补问影响结果的缺口。默认先做出可编辑的版本，再按你的反馈修改。

围绕 BOSS 直聘等平台时，在线简历开头让对方迅速看懂相关性，完整资料和附件证明经历，打招呼语连接当前岗位。推荐列表给个人优势的空间很短，已观察到的招聘端界面约显示 22 个中文字，所以先在 20—22 字内写清一项岗位价值，再用后文展开。

### 11 个 Skill

日常只需要 `zane-career-assets`，它按当前任务读取方法并直接完成；熟悉后可以直接调用专项工具。

| Skill | 你会得到 |
|---|---|
| `zane-career-assets` | 统一入口：方向、找岗位、平台沟通、材料、笔面试、offer、谈薪和入职前准备 |
| `zane-career-portfolio-builder` | 一起完成简历、作品集和投递入口，并安排各自分工 |
| `zane-career-resume-builder` | 从零做简历，或按招聘市场和语言重写 |
| `zane-career-application-greeting` | BOSS 直聘等平台的首条招呼语与后续沟通 |
| `zane-career-portfolio-architecture` | 设计作品集的分层结构与双语投递入口 |
| `zane-career-portfolio-website-design` | 个性化作品集网站：阅读路径、视觉与响应式页面 |
| `zane-career-case-editor-zh` | 把中文案例和求职长文改得像真人写的，保留判断与取舍 |
| `zane-evidence-weighted-case-storytelling` | 按证据强度讲项目故事，不夸大 |
| `zane-portfolio-multi-format-qa` | 发布前检查网页、Word/PDF、链接和数据口径是否一致 |
| `zane-former-employer-data-redactor` | 脱敏前公司数据与敏感信息，再放进作品集 |
| `zane-design-reference-to-prompt` | 把设计参考图转成可复用的生成提示 |

完整用法：[教程](docs/career/guide.md) · [能力目录](docs/career/skill-inventory.md)

---

## 安装

在终端执行，需要 Node.js 和 `npx`。

**只装「过好你的人生」：**

```bash
npx -y skills add ZanePan2027/zpskill -g --skill zane-workbench zane-workbench-curator zane-question-intent-translator zane-agent-identity-card-builder zane-self-insight zane-psychological-support life-decision-guide
```

**只装「走出象牙塔」：**

```bash
npx -y skills add ZanePan2027/zpskill -g --skill zane-career-application-greeting zane-career-assets zane-career-case-editor-zh zane-career-portfolio-architecture zane-career-portfolio-builder zane-career-portfolio-website-design zane-career-resume-builder zane-design-reference-to-prompt zane-evidence-weighted-case-storytelling zane-former-employer-data-redactor zane-portfolio-multi-format-qa
```

**两套都装：**

```bash
npx -y skills add ZanePan2027/zpskill -g --all
```

**Claude Code 插件市场：**

```bash
claude plugin marketplace add ZanePan2027/zpskill
claude plugin install zpskill@zpskill
```

也可以只装单个，例如 `claude plugin install zane-career-assets@zpskill`。

**不用命令行（豆包、WorkBuddy 等）：** 直接告诉 Agent “请从 https://github.com/ZanePan2027/zpskill 安装「过好你的人生」的 7 个 Skills”（或「走出象牙塔」的 11 个），装好后新建对话，说“使用 zane-workbench，帮我……”或“使用 zane-career-assets，帮我……”。各宿主的具体步骤见[人生安装页](docs/life/install.md)和[求职安装页](docs/career/install.md)。

---

## 关于

作者：[Zane](https://github.com/ZanePan2027)。这套方法从具体生活问题里长出来：方向、处境、未来、路线、行动、反馈和共同经历。

本仓库由原来的 zane-life-workbench 和 zane-career-skills 合并而来，旧地址会自动跳转，提交历史保留。

欢迎在 [Issues](https://github.com/ZanePan2027/zpskill/issues) 分享你想完成的事、实际过程和希望改善的地方，公开分享前请自行去除个人与公司敏感信息。[参与贡献](CONTRIBUTING.md) · [版本](VERSION.md) · [更新记录](CHANGELOG.md) · [许可证](LICENSE)（MIT）
