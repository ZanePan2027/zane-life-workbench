# 安装与更新

[English](install.en.md)

## 适用 Agent

豆包、WorkBuddy、Claude Code、Codex，以及其他支持 Skills 的 Agent。按所用客户端选择下面的安装方式。

## 快速安装

Codex、Claude Code 等安装器已列出的 Agent，可在终端执行：

```bash
npx -y skills add ZanePan2027/zane-life-workbench -g --skill "*"
```

这条指令会安装仓库中的全部 Skills。`-g` 表示全局安装；只安装到当前项目时省略 `-g`。`--skill "*"` 选择全部 Skills；在安装器中选择目标 Agent，完成后按客户端要求重载。

需要先安装 Node.js，并确保终端可以使用 `npx`。

也可以直接告诉 Agent：

```text
请从 https://github.com/ZanePan2027/zane-life-workbench 安装全部 Skills，
然后使用 zane-workbench，帮我处理这件事：……
```

## 豆包与 WorkBuddy

在这两个客户端中，直接发送上面的 Agent 安装请求，并说明正在使用哪个客户端。

| 客户端 | 安装位置与操作 |
| --- | --- |
| WorkBuddy | 让 Agent 将仓库 `skills/` 下的各个 Skill 文件夹安装到用户目录的 `.workbuddy/skills/`，保留每个文件夹中的完整内容。安装后到「专家·技能·连接器 → 技能 → 我安装的」查找 `zane-workbench` 并启用。 |
| 豆包 macOS · 本地电脑 | 在「工作任务 → 本地电脑」发送安装请求，让 Agent 将各个 Skill 文件夹安装到 `~/.agents/skills/`。在「连接器 · 技能 · 伙伴 → 技能 → 管理 → 本地」查看，随后在工作任务中调用。 |
| 豆包网页版 · 云电脑 | 打开[豆包网页版](https://www.doubao.com/chat/)，进入「工作 → 云电脑」并发送安装请求，让 Agent 确认当前云端支持的持久技能目录后安装。 |

豆包云电脑与本地电脑的技能分别安装，不会自动互通。云端长期保留技能可使用平台技能管理入口或 `user_skills` 目录；普通云端临时环境中的安装会随沙箱清理。浏览器也能发起工作任务，具体入口见豆包官方[打开豆包工作](https://www.doubao.com/work/docs/zh-cn/articles/462191106451-access)与[工作任务模式](https://www.doubao.com/work/docs/zh-cn/articles/047323472965-work-task-mode)。

若安装器的列表没有这两个名字，直接采用上述方式。安装后的入口应为 `<技能目录>/zane-workbench/SKILL.md`，不要在技能目录中再套一层仓库文件夹。新建对话后说“使用 zane-workbench，帮我……”，开始第一件事。

## 开始使用

告诉 Agent：

```text
请使用 zane-workbench，把当前项目文件夹设为我的人生工作台。
沿用已有资料与规则，建立够用的入口，再帮我处理这件事：……
```

先在Agent中打开准备长期使用的文件夹；尚未选择位置时，让Agent引导创建。Skill安装目录存放方法，工作台文件夹存放自己的资料与进展。手头材料可以直接放进约定资料入口，无需先分类。

以后打开同一个工作台项目，直接说“接着上次”。只有换了项目、原目录不可访问或位置有歧义时才重新定位。临时任务可以直接问；完整步骤见[使用教程](guide.md)。

## 更新

先保留自己修改过的 Skill 文件，再执行同一条快速安装指令，按安装界面更新。产品目前保持1.0，文件内容仍会继续修订；不要仅凭版本号相同跳过更新，以仓库修订日期和提交识别内容。

```bash
npx -y skills add ZanePan2027/zane-life-workbench -g --skill "*"
```

[返回首页](../README.md)
