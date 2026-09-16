# 安装与更新

## 安装整套方法

在 Claude Code、Codex 等支持 Agent Skills 的工具中，可以让 Agent 从本仓库安装，也可以执行：

```bash
npx -y skills add ZanePan2027/zane-life-workbench -g --all
```

`-g` 表示全局安装；安装到当前项目时省略 `-g`。按安装界面选择要使用的 Agent，完成后按宿主要求重载。

输入“请使用 zane-workbench，帮我处理这件事：……”开始。

## 更新

告诉 Agent：“比较本仓库与我已安装的版本，更新过好你的人生。”保留自己修改过的方法，再按所用 Skill 管理器的更新流程操作。

本次产品仍为1.0，但文件内容已更新；不要仅凭版本号相同跳过更新。当前源码标签为 `v1.0.0`，对应2026-09-16修订。仓库以本次已核验的1.0内容重新建立，旧Git历史不再包含于本仓库。需要固定内容时核对修订日期、完整提交和包摘要。切换前备份自己修改的文件。

[最新Release](https://github.com/ZanePan2027/zane-life-workbench/releases/latest)提供完整ZIP及SHA256SUMS。若此前通过随包安装器安装，解压新包后使用其 `install.py --skills-dir <宿主实际Skill目录> --upgrade`；安装器按内容处理同版本更新并保留回滚检查点。下载包与源码快照对应的日期见VERSION.md。

## 手动安装

从仓库 `skills/` 目录取得各个 Skill 文件夹，按宿主说明放入它的 Skill 目录。每个文件夹以 `SKILL.md` 为入口，相关方法和模板随目录一起保留。

## 开始保存工作

告诉 Agent 想使用的工作台文件夹。它会读取已有导航，或从本次成果建立记录。Skill 安装目录存放方法，个人工作台文件夹存放自己的资料和进展。

[返回首页](../README.md)
