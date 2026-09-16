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
请使用 zane-workbench，把当前项目文件夹设为我的人生工作台。
沿用已有资料与规则，建立够用的入口，再帮我处理这件事：……
```

先在Agent中打开准备长期使用的文件夹；尚未选择位置时，让Agent引导创建。Skill安装目录存放方法，工作台文件夹存放自己的资料与进展。手头材料可以直接放进约定资料入口，无需先分类。

以后打开同一个工作台项目，直接说“接着上次”。只有换了项目、原目录不可访问或位置有歧义时才重新定位。临时任务可以直接问；完整步骤见[使用教程](guide.md)。

## 更新

先保留自己修改过的 Skill 文件，再执行同一条快速安装指令，按安装界面更新。产品目前保持1.0，文件内容仍会继续修订；不要仅凭版本号相同跳过更新，以仓库修订日期和提交识别内容。

```bash
npx -y skills add ZanePan2027/zane-life-workbench -g --all
```

[返回首页](../README.md)
