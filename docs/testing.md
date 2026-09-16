# 验证范围与已知限制 / Validation and known limitations

修订日期 / Revision: 2026-09-16。产品1.0；五个组件1.0.0。外部验收待完成。

## 本次首次使用修订

默认入门调整为连接或创建工作台、接入相关资料、处理当前问题、保存并继续。同一项目续接自行读取入口，不要求反复指定文件夹；临时任务仍可直接处理。

- 开发工作区103项工程测试通过，包括来源分页、引用、安装回滚和发布核验；Skill同步、124个入口与路由检查通过。部分测试属于开发工具，未作为独立测试集随公开仓库分发。
- 使用交付包进行内部合成场景：独立Codex子Agent从零建台，无材料时没有虚构画像或事项；另一个子Agent沿用已有规则、原件与手工唯一状态，实际完成课程比较并保存进展。
- 不带前次会话历史的子Agent从同一工作区恢复比较与暂停点，继续产出沟通草稿，未重问路径，也没有把“建议”记成“已决定、已报名或已发送”。这验证了给定工作区内的文件接续，不证明所有宿主都自动打开正确项目。
- 已有空文件夹的独立场景完成就地接入和一句翻译，没有删除重建、生成第二层工作台或先索取人生档案。
- 初次测试中两次出现调用者把来源角色写成数组的配置错误，检查发现后修复；一次读取未返回正文，Agent随后显式读取原件。记录保留失败与恢复过程，不能把首次执行称为全程无误。已在来源接口补充单个角色字符串与手工状态的配置示例。
- 补充配置示例后，以最终交付包再做一次独立空目录建台与翻译场景：正确生成手工状态映射，读取155字符原文，引用检查通过，无失败或重试。最终包与首轮包的方法差异仅为这份来源接口说明。
- 中英文上手、安装、接续说明及两张示意图同步更新；快速指令与直接告诉Agent安装两种入口保留。

这些是开发者主持的内部测试，不是外部真实用户验收。测试材料为合成输入，不包含作者的私人档案。

## 历史证据与限制

此前可靠性修订的内部合成测试曾完成10页、27449字符读取，在回答中采用末页更正；初答后的新反馈修订同一成果，另一个无前文子Agent从文件恢复当前状态。保存的重现分页通过覆盖检查，但不是首次调用日志，也不能证明模型理解。长输入主要由重复教学记录组成，不能证明复杂长文全面稳定；历史结果也不自动证明本次修改后的所有行为。

此前五题个人回归的核心判断通过，但未读完全部所选来源分页，完整取源过程没有通过。工具可以返回正文，不证明模型已经完整阅读或理解。

## 尚未证明

尚无外部真实用户验收或长期生活效果证据。Claude、其他宿主与Windows没有完成本次原生行为实测。同一项目是否自动加载入口受宿主功能与使用方式影响；换工具需要打开或授权访问原工作台。没有文件能力的聊天环境使用接续摘要，不宣称自动保存或永久记忆。新文件在收录或相关任务中读取，不在会话外后台监控。

## 从零开始与反馈

先在Agent中连接或创建一个工作台项目，放入手头相关材料，也可以没有资料。Agent整理入口后读取当前问题需要的正文，形成并保存成果；下次打开同一项目直接继续。临时问题无需建台。

发现问题时，通过GitHub Issues提供去除隐私的复现步骤、宿主、修订日期或提交、期望和实际结果。不要上传私人原件、账号凭据或他人的个人信息。正式发布与工程检查都不替代真实用户验收。

## English

This revision starts ongoing use by connecting or creating a workspace, taking in relevant material, working on one task, and saving progress. A session in the same project reads its entries without asking for the folder again. One-off tasks can start directly.

The development workspace passed 103 engineering tests, plus Skill synchronization and checks for 124 managed entries. Some tests cover development tools and are not shipped as an independent public test suite.

Internal synthetic scenarios used the delivery package: a fresh setup without invented personal facts; adaptation of an existing project while preserving rules, originals, and a single Markdown task state; a separate session without prior conversation that resumed and drafted a message without claiming a decision, enrollment, or sending; and in-place setup of an existing empty folder while completing a short translation. These show behavior within a supplied workspace, not automatic project selection across all hosts.

Two initial scenarios incorrectly used arrays for source roles, then corrected them after checks failed. One read returned no source text, followed by an explicit read of the original. The records retain these failures and recoveries. The source contract now includes a string-role example and explains how to bind a manual Markdown state without treating it as a JSON event. Initial execution was not error-free. After clarifying the format, a separate run with the final package completed empty-folder setup and translation, read 155 source characters, and passed reference checks without failures or retries. The only method difference from the first test package is the source-contract clarification.

Earlier reliability evidence includes ten-page reading of 27,449 characters, feedback correction, and fresh-session continuation. Reproduced page captures were coordinator reruns, not the initial call logs; neither captures nor mostly repetitive long input establish general reading reliability. Historical results do not validate all behavior after this revision. A previous personal regression had useful judgments but incomplete source reading.

External real-user acceptance, long-term outcomes, native behavior on other hosts, and Windows remain unverified. When changing tools, open or authorize the same workspace folder. Ordinary chat uses saved continuation notes. Adding a file does not trigger background monitoring outside a session. Report sanitized reproduction steps, host, exact revision, and expected versus actual behavior; never publish private source material or credentials.
