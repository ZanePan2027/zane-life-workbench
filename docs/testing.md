# 验证范围与已知限制 / Validation and known limitations

修订日期 / Revision: 2026-09-17。产品1.0；五个组件1.0.0。外部验收待完成。

## 事实与交付一致性修订

共享方法补上缺失值、数量口径冲突、承诺边界及交付前一致性核对。商业包另补投入阈值推导，相关商业方法不随人生仓库分发。

开发工作区105项工程测试、Skill同步与路由检查通过。内部行为检查包括一份既有投放材料重放、一个新合成经营场景和一个新合成职业场景。主持Agent读取实际产物按预先记录的条件核验；没有普通AI或其他产品对照，不据此声称质量提升幅度或产品优劣。

首轮投放重放仍把有歧义的关注数称为新增，虽然保留了归因未知；这不足以通过数量口径检查。补充新增与累计的区分后，独立复测明确保留该冲突，缺失值、承诺、条件阈值与行动顺序的目标检查通过；两轮均未输出预算百分比，不称验证了该计算。新经营与职业场景在首轮方法下完成条件成本计算、未知值与服务边界处理、步骤依赖核对；二者未在最后一句澄清后重跑。本次没有重新执行人生任务、跨宿主行为或真实用户验收，也没有联网验证外部行业基准。

## 共享整理器的三模式修订

本轮补齐商业与职业模板的来源映射，将`--minimal`初始化扩展到life、work、career三种模式；已有目录继续就地适配，不运行初始化覆盖。来源角色依据当前任务解释：商业使用本业务目标与状态，职业使用岗位任务用途与当前进度，不因此加载个人全人生档案。人生仓库仍分发人生主入口及共享组件，不包含商业或职业主入口。

105项开发工程测试通过，包括新增的两种最小工作区来源绑定、其他主体数据不进入已选正文、已有目录不被重建、模板缺失时不留下半成品，以及三包共装和升级回滚。其余合成行为与外部验证范围见各次记录；工程测试不等于真实用户效果。

## 此前首次使用修订

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

The September 17 shared method revision handles missing records, inconsistent quantity definitions, confirmed commitments, and delivery consistency. Business-specific investment calculations were updated in the separate local business package and are not distributed here. The development suite passed 105 tests and synchronization/routing checks. Internal behavioral checks covered replay of one existing advertising task and two new synthetic business and career tasks. The coordinating Agent reviewed outputs against prerecorded criteria; there was no ordinary-AI or competing-product control, and no causal or superiority claim is supported. The first replay still treated an ambiguous follower count as new; attribution uncertainty did not resolve this. After clarifying additions versus totals, a separate replay retained the conflict and met the targeted checks for missing values, commitments, conditional thresholds, and action order. Neither replay reported budget percentages, so that calculation was not exercised. The new business and career scenarios were run before that final clarification and were not rerun afterward. This revision did not retest life-specific tasks, other hosts, real users, or online verification of industry benchmarks.

The shared curator now provides source maps for business and career profiles and supports minimal initialization in all three modes. Existing folders are still adapted in place. Source roles describe the active business or job task rather than requiring a personal life profile. This repository distributes the life entry and shared components, not the business or career entry Skills. The development suite passed 105 tests, including minimal profiles, scoped source binding, preservation of existing folders, incomplete-template failure, co-installation, upgrade, and rollback. This is engineering evidence, not real-user outcome evidence.


This revision starts ongoing use by connecting or creating a workspace, taking in relevant material, working on one task, and saving progress. A session in the same project reads its entries without asking for the folder again. One-off tasks can start directly.

The development workspace passed 103 engineering tests, plus Skill synchronization and checks for 124 managed entries. Some tests cover development tools and are not shipped as an independent public test suite.

Internal synthetic scenarios used the delivery package: a fresh setup without invented personal facts; adaptation of an existing project while preserving rules, originals, and a single Markdown task state; a separate session without prior conversation that resumed and drafted a message without claiming a decision, enrollment, or sending; and in-place setup of an existing empty folder while completing a short translation. These show behavior within a supplied workspace, not automatic project selection across all hosts.

Two initial scenarios incorrectly used arrays for source roles, then corrected them after checks failed. One read returned no source text, followed by an explicit read of the original. The records retain these failures and recoveries. The source contract now includes a string-role example and explains how to bind a manual Markdown state without treating it as a JSON event. Initial execution was not error-free. After clarifying the format, a separate run with the final package completed empty-folder setup and translation, read 155 source characters, and passed reference checks without failures or retries. The only method difference from the first test package is the source-contract clarification.

Earlier reliability evidence includes ten-page reading of 27,449 characters, feedback correction, and fresh-session continuation. Reproduced page captures were coordinator reruns, not the initial call logs; neither captures nor mostly repetitive long input establish general reading reliability. Historical results do not validate all behavior after this revision. A previous personal regression had useful judgments but incomplete source reading.

External real-user acceptance, long-term outcomes, native behavior on other hosts, and Windows remain unverified. When changing tools, open or authorize the same workspace folder. Ordinary chat uses saved continuation notes. Adding a file does not trigger background monitoring outside a session. Report sanitized reproduction steps, host, exact revision, and expected versus actual behavior; never publish private source material or credentials.
