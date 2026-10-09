# 安装与更新

[English](install.en.md)

## 适用 Agent

豆包、WorkBuddy、Claude Code、Codex，以及其他支持 Skills 的 Agent。按所用客户端选择下面的安装方式。

## 快速安装

Codex、Claude Code 等安装器已列出的 Agent，可在终端执行，需要 Node.js 和 `npx`：

```bash
npx -y skills add ZanePan2027/zpskill -g --skill zane-career-application-greeting zane-career-assets zane-career-case-editor-zh zane-career-portfolio-architecture zane-career-portfolio-builder zane-career-portfolio-website-design zane-career-resume-builder zane-design-reference-to-prompt zane-evidence-weighted-case-storytelling zane-former-employer-data-redactor zane-portfolio-multi-format-qa
```

这会安装完整求职工具箱。`--all` 会安装全部 Skills，并装进安装器支持的所有 Agent，无需逐个选择；安装后按客户端要求重载。只想装到某一个 Agent 时，改用 `--skill "*" --agent <名称>`。只在当前项目使用时，省略 `-g`。

也可以直接告诉 Agent：

```text
请从 https://github.com/ZanePan2027/zpskill 安装「走出象牙塔」的 11 个 Skills（zane-career-application-greeting、zane-career-assets、zane-career-case-editor-zh、zane-career-portfolio-architecture、zane-career-portfolio-builder、zane-career-portfolio-website-design、zane-career-resume-builder、zane-design-reference-to-prompt、zane-evidence-weighted-case-storytelling、zane-former-employer-data-redactor、zane-portfolio-multi-format-qa），
然后使用 zane-career-assets，帮我处理这件事：……
```

## 豆包与 WorkBuddy

在这两个客户端中，直接发送上面的 Agent 安装请求，并说明正在使用哪个客户端。

| 客户端 | 安装位置与操作 |
| --- | --- |
| WorkBuddy | 让 Agent 将仓库 `skills/` 下的各个 Skill 文件夹安装到用户目录的 `.workbuddy/skills/`，保留每个文件夹中的完整内容。安装后到「专家·技能·连接器 → 技能 → 我安装的」查找 `zane-career-assets` 并启用。 |
| 豆包 macOS · 本地电脑 | 在「工作任务 → 本地电脑」发送安装请求，让 Agent 将各个 Skill 文件夹安装到 `~/.agents/skills/`。在「连接器 · 技能 · 伙伴 → 技能 → 管理 → 本地」查看，随后在工作任务中调用。 |
| 豆包网页版 · 云电脑 | 打开[豆包网页版](https://www.doubao.com/chat/)，进入「工作 → 云电脑」并发送安装请求，让 Agent 确认当前云端支持的持久技能目录后安装。 |

豆包云电脑与本地电脑的技能分别安装，不会自动互通。云端长期保留技能可使用平台技能管理入口或 `user_skills` 目录；普通云端临时环境中的安装会随沙箱清理。浏览器也能发起工作任务，具体入口见豆包官方[打开豆包工作](https://www.doubao.com/work/docs/zh-cn/articles/462191106451-access)与[工作任务模式](https://www.doubao.com/work/docs/zh-cn/articles/047323472965-work-task-mode)。

若安装器的列表没有这两个名字，直接采用上述方式。安装后的入口应为 `<技能目录>/zane-career-assets/SKILL.md`，不要在技能目录中再套一层仓库文件夹。新建对话后说“使用 zane-career-assets，帮我……”，开始第一件事。

## 开始使用

日常从 `zane-career-assets` 进入，提供当前任务与手边材料。可以先整理一段经历、比较两个岗位、写一段简历，或练习面试。看[完整使用示例](guide.md)。

## 更新与保存

告诉 Agent：“比较这个仓库与我安装的版本，保留我的本地修改后更新走出象牙塔。”更新时核对实际文件与修订，不只看版本号。

Skill 安装目录保存方法。单次任务无需建立目录；需要保存个人材料时沿用当前项目，位置已知不重复询问。个人文件不放进Skill安装目录。

[返回首页](README.md)
