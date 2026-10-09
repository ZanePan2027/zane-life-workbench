# 保存与继续

单次回答或局部改句直接交付。制作文件时沿用用户当前项目或指定输出位置，保留原简历，候选另存；没有必要让用户先创建某种标准目录。位置已明确就不重问。

需要多轮修改、多个岗位版本或模拟面试接续时，保存最小记录：本次岗位与用途、依据的材料、当前采用版本、影响后续的纠正与偏好、未解决事项和真实暂停点。可以是一份Markdown，或沿用已有zane-career-assets-state.json；不同时新建第二套唯一状态。

用户说继续时，先读取当前目录已有入口、当前稿和记录。不同公司或岗位分别识别，避免将A岗谈薪和B岗面试混写。模拟保存问过的问题、真实回答、反馈、轮到谁；没有回答的题不能补成用户已答。位置不明、访问失败或多个任务不能判断时再问一个必要问题。

可选工具用法：

```bash
python3 scripts/career_assets_state.py init --state <项目>/zane-career-assets-state.json --project <名称> --scope resume
python3 scripts/career_assets_state.py check --state <项目>/zane-career-assets-state.json --action build-resume
```

默认允许候选制作。只有用户主动要求逐阶段确认时设置`mode --review-mode staged --pause-at content,visual --note <本人要求>`；回到直接交付用`mode --review-mode deliver --note <当前要求>`。

多资产的检查/确认用`decide --artifact <名称> --gate qa --status checked --note <实际检查> --evidence <证据路径>`及`--gate final_confirmation --status approved`记录。`check --action release --artifact <名称>`只核这一项，不让一份简历的确认代替整个网站的确认。

事实或目标改变时先修改依据和成果，再用`reopen --gate evidence_position --affects resume,website --note <原因>`标记受影响旧版需复核；新候选通过实际检查后更新。手工记录采用相同语义即可。保存记录不表示工具在后台监视文件。

无文件能力的聊天可交付可复制摘要；明确其需要用户保存，不声称永久记忆。
