# 走出象牙塔

简体中文 | [English](README.en.md)

> 从不知道投什么，到写好材料、聊到面试、判断 offer。解决你眼前的求职问题。

[![Version](https://img.shields.io/badge/version-v1.0.0-2563EB.svg?style=flat-square)](VERSION.md)
[![License](https://img.shields.io/badge/license-MIT-16A34A.svg?style=flat-square)](../../LICENSE)

**面向入职前各环节的 AI 求职工具箱，重点服务实习生、应届毕业生和工作 1—2 年的新人。** 有多年经验、正在换工作的人也可以用，按实际资历处理。

**支持：豆包、WorkBuddy、Claude Code、Codex，以及其他支持 Skills 的 Agent。**

[快速开始](#快速开始) · [可以处理的事](#可以处理的事) · [使用教程](guide.md) · [能力目录](skill-inventory.md) · [安装与更新](install.md)

![从当前求职问题直接开始](career-assets-flow.zh-CN.svg)

把旧简历、岗位截图、项目材料、面试问题或 offer 给 Agent，直接说需要什么。从手头最需要解决的一件事开始。

<a id="安装"></a>

## 快速开始

### 1. 安装

在终端执行：

```bash
npx -y skills add ZanePan2027/zpskill -g --skill zane-career-application-greeting zane-career-assets zane-career-case-editor-zh zane-career-portfolio-architecture zane-career-portfolio-builder zane-career-portfolio-website-design zane-career-resume-builder zane-design-reference-to-prompt zane-evidence-weighted-case-storytelling zane-former-employer-data-redactor zane-portfolio-multi-format-qa
```

也可以直接告诉 Agent：

```text
请从 https://github.com/ZanePan2027/zpskill 安装「走出象牙塔」的 11 个 Skills（zane-career-application-greeting、zane-career-assets、zane-career-case-editor-zh、zane-career-portfolio-architecture、zane-career-portfolio-builder、zane-career-portfolio-website-design、zane-career-resume-builder、zane-design-reference-to-prompt、zane-evidence-weighted-case-storytelling、zane-former-employer-data-redactor、zane-portfolio-multi-format-qa），
然后使用 zane-career-assets，帮我处理这件事：……
```

命令安装适用于 Codex、Claude Code 等安装器已列出的 Agent，需要 Node.js 和 `npx`。豆包、WorkBuddy 请使用上面的 Agent 安装请求，具体步骤见[安装说明](install.md)。

### 2. 从手头的任务开始

```text
请使用 zane-career-assets。这是我的旧简历和想投的岗位。
我主要用 BOSS 直聘，请帮我重做一份简历，
同时写好在线简历的个人优势开头和这个岗位的打招呼语。
先直接做出可编辑版本，我看完再提修改。
```

已有的信息直接使用，只补问影响结果的缺口。默认完成你要的候选稿或文件，再按反馈修改；想先确认文案再设计，也可以直接说。

## 可以处理的事

| 当前问题 | 可以得到 |
| --- | --- |
| 不知道适合投什么，没有实习怎么写？ | 方向比较、真实经历取材与可尝试的小项目 |
| 到哪里找实习／校招／社招，怎样看 JD？ | 岗位筛选条件、可核查机会、资格与匹配判断 |
| BOSS 直聘开头写什么，打招呼总没回应？ | 在线简历首句、个人优势、岗位招呼语与沟通调整 |
| 旧简历要重做，想做英文版 | 针对岗位和市场的内容、版式及所需文件 |
| 需要作品集，但项目不多 | 可展示作品选择、案例内容、文档或网站 |
| 笔试、作业和面试不知道怎么准备 | 练习方案、回答改进、一问一答的模拟面试 |
| offer 怎么选，怎样谈薪或回复？ | 同口径待遇比较、待核实条款、谈薪与回复草稿 |
| 签约、背调、到岗前要准备什么？ | 针对当前情况的手续梳理、核实问题与时间安排 |

## 围绕 BOSS 直聘等平台使用

在线简历开头让对方迅速看懂相关性；完整资料和附件简历证明经历；打招呼语连接当前岗位；作品集按需展示作品与过程；后续沟通争取把具体问题聊清楚。

推荐列表留给个人优势的空间很短：已观察到的招聘端界面约显示 22 个中文字。先在 20—22 字内写清一项岗位价值，再用后文展开经历，让搜索列表和完整简历也有内容可读。Agent 会按你提供的界面调整。[各界面展示与写法](../../skills/zane-career-assets/references/platform-evidence.md)

[看使用示例：旧简历、BOSS 沟通、作品集、面试与 offer](guide.md)

## 继续修改与保存

单次任务可以直接完成。需要下次继续时，让 Agent 在现有项目中保存当前版本和暂停点；下次在同一项目说“接着上次”。位置已知不必反复指定文件夹；纯聊天环境可保留简短摘要。

## 能力与验证

工具箱包含 11 个 Skill。日常只需要 `zane-career-assets`，它按当前任务读取方法并直接完成；熟悉后可直接调用[专项工具](skill-inventory.md)。

欢迎通过 Issues 分享使用反馈，请先去除个人与公司敏感信息。[版本检查记录](testing.md)。

## 来源与许可证

参考 DBS 的按任务选择方法、按需读取与接续思路，结合求职材料制作中的实际问题重新设计。[设计取舍与来源](provenance.md)。

本仓库采用 [MIT License](../../LICENSE)。作者：Zane
