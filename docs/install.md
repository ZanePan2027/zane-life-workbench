# 安装与更新

[English](install.en.md)

## 快速安装

在终端执行：

```bash
npx -y skills add ZanePan2027/zane-life-workbench -g --all
```

这条指令会安装仓库中的全部 Skills。`-g` 表示全局安装；只安装到当前项目时省略 `-g`。按安装界面选择 Claude Code、Codex 等要使用的 Agent，完成后按宿主要求重载。

需要先安装 Node.js，并确保终端可以使用 `npx`。

也可以直接告诉 Agent：

```text
请从 https://github.com/ZanePan2027/zane-life-workbench 安装全部 Skills，
然后使用 zane-workbench，帮我处理这件事：……
```

## 开始使用

告诉 Agent：

```text
请使用 zane-workbench，帮我处理这件事：……
```

需要保存进展时，告诉 Agent 想使用的工作台文件夹。Skill 安装目录存放方法，个人工作台文件夹存放自己的资料与进展。

## 更新

先保留自己修改过的 Skill 文件，再执行同一条快速安装指令，按安装界面更新。产品目前保持1.0，文件内容仍会继续修订；不要仅凭版本号相同跳过更新，以仓库修订日期和提交识别内容。

```bash
npx -y skills add ZanePan2027/zane-life-workbench -g --all
```

[返回首页](../README.md)
