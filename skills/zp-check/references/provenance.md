# 来源与边界

## 依据

| 问题 | 依据 | 对我们的含义 |
|---|---|---|
| 多轮对话越聊越偏 | Laban、Hayashi、Zhou、Neville 2025，《LLMs Get Lost In Multi-Turn Conversation》（arXiv 2505.06120）：主流模型多轮平均下降约 39%，不可靠性上升 112%；常在前几轮做假设并过早给出最终方案，走错后不恢复；系统自动的回顾等补救不够 | 偏了就把要求一次说全，开新对话 |
| 过度信任 AI 的产出 | Passi、Vorvoreanu 2022，《Overreliance on AI: Literature Review》（微软）；Lee 等 2025，CHI，《The Impact of Generative AI on Critical Thinking》（自评调查，相关而非因果）：对 AI 越有信心，批判性思考越少，重心转向核实与整合 | 把核实当成固定动作，不靠感觉 |
| AI 附和用户 | Sharma 等 2023，《Towards Understanding Sycophancy in Language Models》，ICLR 2024 | 对泛泛的夸奖按附和处理 |
| 非专家不会写提示词 | Zamfirescu-Pereira 等 2023，CHI，《Why Johnny Can't Prompt》 | 卡住时先 `zp-question` 钉锚点 |

另有一条来自使用现场：脚本打印“已提交”，实际并没有发出去，要读回真实状态才发现。这类“工具说成功但没成功”的情况，是把“看到成品”放进流程的直接原因。

## 边界

- 这是方法，不是保证。复核能发现很多问题，发现不了所有问题；两个都会出错的来源互相印证，也可能一起错。
- 研究多数是实验或自评调查，样本和任务与你的具体场景不同；这里只取它们的方向，不取具体数字去预测你的结果。
- 不替代专业意见：涉及医疗、法律、财务的结论，核实要找相应的专业来源或专业人士。
- 本技能不评判用户该不该做某件事，这是 `zp-judge` 的事；也不替用户把问题写清，这是 `zp-question` 的事。
