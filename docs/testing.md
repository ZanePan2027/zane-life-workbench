# 验证范围与已知限制 / Validation and known limitations

修订日期 / Revision: 2026-09-16。产品1.0；五个组件和安装包1.0.0。外部验收待完成。

## 已有证据

- 最终方法与工具源码通过开发工作区93项工程测试，覆盖来源分页还原、来源变化后的旧续读拒绝、任务分流、依赖查找、安装及回滚等；这些测试并非93个真实用户案例。
- 使用合成资料的原生Codex新会话实际完成：从散放原件建立工作台并产出择业比较；收到新条件后撤回旧建议并改写成果和原事项；再由全新会话恢复最新判断及未发送状态。
- 建台、反馈纠正和冷启动实际使用本次最终包。首答使用的先行包有一个取源分支差异；首答3组实际取源调用在两版中结果相同。这项等价核对不是重新运行首答。
- 五题内部个人回归的核心判断通过；该会话没有读完全部所选来源分页，完整取源过程未通过。工具可完整返回正文，不证明模型已经完整读取或理解。
- 分发清单及内容复核未发现作者私人档案、财务、任职原件、聊天记录或真实事项进入公开包。模板不预填作者个人目标。私人测试原件和记录不公开。

## 尚未证明

这些是开发者主持的内部测试，没有完成外部真实用户验收，也没有证明长期生活效果。Claude本轮只有入口与工具层检查，未完成新版原生判断验收；其他宿主及Windows未实测。纯聊天环境有起步方法，但不具备文件工具的自动保存能力。模型仍可能遗漏材料或误判，来源检查也不能证明现实事实正确。

## 从零开始与反馈

安装后提供当前问题及手头材料即可，不要求先填完整人生档案。AI先完成当前能做的成果，再保存必要的来源与进展。换会话时提供工作台位置。若没有文件工具，保存接续摘要，在下次聊天贴回。

发现问题时，可以通过GitHub Issues提供去除隐私的复现步骤、所用宿主、修订日期或包摘要、期望与实际结果。不要上传私人原件、账号凭据或他人的个人信息。真实用户验收需要对应明确包内容，记录实际使用、成果、反馈与未解决问题。

## English

The final method and tool sources passed 93 engineering tests in the development workspace. These are not 93 real-user cases. Fresh native Codex sessions using synthetic material completed onboarding from loose files, a useful comparison, revisions after changed conditions, and continuation from saved state. Onboarding, correction, and cold restart used the final package. The initial answer used an earlier package with one source-selection branch difference; its three actual source calls returned identical results on both engines. This equivalence check is not a rerun of the initial answer.

A five-question internal personal regression passed the core judgment checks but did not read every selected source page. The complete source-reading process therefore did not pass. Availability of source text is not proof that a model read or understood it.

The distribution was checked for private author material and contains general methods, tools, and templates, without the author's personal records or prefilled goals. Private test inputs and logs are not published. Data handling during use depends on your AI provider and settings.

External real-user acceptance and long-term outcomes remain unverified. This revision has not passed native judgment testing across all hosts; Windows was not tested. In ordinary chat, continuation requires saving and reusing a note rather than automatic file persistence. Version 1.0 does not imply external acceptance.

To start, share your current task and existing material. Let the Agent produce useful work and save only what is needed to continue. For a bug report, share a sanitized reproduction, host, exact revision or checksum, and expected versus actual behavior. Never publish private source material or credentials.
