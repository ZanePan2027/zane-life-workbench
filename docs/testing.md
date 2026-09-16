# 验证范围与已知限制 / Validation and known limitations

修订日期 / Revision: 2026-09-16。产品1.0；五个组件和安装包1.0.0。外部验收待完成。

## 已有证据

- 本次开发工作区复查通过103项工程测试，覆盖来源分页、显式领域、同会话同版本复用、保存正文覆盖检查、反馈依赖、安装及回滚和发布候选核验等。部分测试针对开发工作台和发布工具，并非公开包内的独立测试，也不是103个真实用户案例。
- 本轮内部合成测试从本次1.0.0包开始：独立Codex子Agent实际读取10页、27449字符，在比较中采用末页更正；初答后收到排班变化，更新同一成果并撤回失效理由。另一个无前会话历史的子Agent从保存文件恢复最新条件和下一步，未将建议当成使用者已经接受或签约。
- 保存的重现分页通过连续正文覆盖核验；这些是主持者按相同参数重现的页文件，不能替代首次原始调用日志，也不能证明模型理解。长材料主要是重复教学记录，本场景通过不能证明复杂长文全面稳定。
- 此前从散放材料建台、形成比较、反馈改判与新会话接续的内部证据保留；本轮补测聚焦长材料取源、纠正与接续。
- 五题内部个人回归的核心判断通过；该会话没有读完全部所选来源分页，完整取源过程未通过。工具可完整返回正文，不证明模型已经完整读取或理解。
- 分发清单及内容复核未发现作者私人档案、财务、任职原件、聊天记录或真实事项进入公开包。模板不预填作者个人目标。私人测试原件和记录不公开。

## 尚未证明

这些是开发者主持的内部测试，没有完成外部真实用户验收，也没有证明长期生活效果。Claude本轮只有入口与工具层检查，未完成新版原生判断验收；其他宿主及Windows未实测。纯聊天环境有起步方法，但不具备文件工具的自动保存能力。模型仍可能遗漏材料或误判，来源检查也不能证明现实事实正确。

## 从零开始与反馈

安装后提供当前问题及手头材料即可，不要求先填完整人生档案。AI先完成当前能做的成果，再保存必要的来源与进展。换会话时提供工作台位置。若没有文件工具，保存接续摘要，在下次聊天贴回。

发现问题时，可以通过GitHub Issues提供去除隐私的复现步骤、所用宿主、修订日期或包摘要、期望与实际结果。不要上传私人原件、账号凭据或他人的个人信息。真实用户验收需要对应明确包内容，记录实际使用、成果、反馈与未解决问题。

## English

The development workspace passed 103 engineering tests in this review, including paged sources, explicit topic selection, same-session reuse, captured-body coverage, dependency lookup, installation, rollback, and release-candidate verification. Some tests cover private development adapters and publishing tools; this is not a standalone test suite shipped in the public package or 103 real-user cases.

In the current internal synthetic test, an independent Codex subagent used this 1.0.0 package, read 27,449 characters over ten pages, and used a correction on the last page. New scheduling information was supplied only after the initial answer; the Agent updated the same result and withdrew the obsolete reason. A separate subagent without the earlier conversation resumed from saved files and distinguished advice from an accepted offer or signed contract. Reproduced page captures passed continuous-body coverage checks. Those captures were recreated by the test coordinator; they are not the first call logs and do not prove model understanding. The long input mostly consists of repetitive teaching records, so this scenario does not establish reliability on complex long documents.

Earlier internal evidence for onboarding from loose material, comparison, correction, and continuation remains historical evidence. This revision adds long-source reading, correction, and fresh-session continuation checks.

A five-question internal personal regression passed the core judgment checks but did not read every selected source page. The complete source-reading process therefore did not pass. Availability of source text is not proof that a model read or understood it.

The distribution was checked for private author material and contains general methods, tools, and templates, without the author's personal records or prefilled goals. Private test inputs and logs are not published. Data handling during use depends on your AI provider and settings.

External real-user acceptance and long-term outcomes remain unverified. This revision has not passed native judgment testing across all hosts; Windows was not tested. In ordinary chat, continuation requires saving and reusing a note rather than automatic file persistence. Version 1.0 does not imply external acceptance.

To start, share your current task and existing material. Let the Agent produce useful work and save only what is needed to continue. For a bug report, share a sanitized reproduction, host, exact revision or checksum, and expected versus actual behavior. Never publish private source material or credentials.
