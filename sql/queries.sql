-- 1. 基础统计：总玩家数、平均学习时间、平均ROI
SELECT 
    COUNT(DISTINCT player_id) AS total_players,
    ROUND(AVG(study_hours_week), 2) AS avg_study_hours,
    ROUND(AVG(realized_roi), 2) AS avg_roi
FROM poker_raw;

-- 2. 对比分析：破产玩家 (went_broke=1) vs 未破产玩家 的 心理控制与资金管理差异
SELECT 
    went_broke,
    COUNT(*) AS player_count,
    ROUND(AVG(tilt_control), 2) AS avg_tilt_control,
    ROUND(AVG(bankroll_mgmt), 2) AS avg_bankroll_mgmt
FROM poker_raw
GROUP BY went_broke;

-- 3. 谁是“技术流”？查看技能值 (skill) 前10名玩家的ROI和盈利率
SELECT 
    player_id, 
    skill, 
    ROUND(realized_roi, 2) AS roi,
    ROUND(win_rate, 2) AS win_rate
FROM poker_raw
ORDER BY skill DESC
LIMIT 10;

-- 4. 高级SQL：使用窗口函数 (Window Function) 对玩家进行排名
-- 根据 real ROI 给所有玩家排名，并在旁边显示他的技能分
SELECT 
    player_id,
    ROUND(realized_roi, 2) AS roi,
    RANK() OVER (ORDER BY realized_roi DESC) AS roi_rank,
    skill
FROM poker_raw
LIMIT 20;