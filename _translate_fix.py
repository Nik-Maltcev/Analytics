# -*- coding: utf-8 -*-
"""Fix remaining Chinese text after first translation pass."""

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    count = 0
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            count += 1
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  {filepath}: {count}/{len(replacements)}")

# ============================================================
# Step2EnvSetup.vue - partial replacements & comments
# ============================================================
replace_in_file('frontend/src/components/Step2EnvSetup.vue', [
    # Partial replacement fix
    ("每ч活跃", "Активных/ч"),
    ("模拟环境已Подготовка завершена，可以开始运行模拟", "Среда симуляции готова к запуску"),
    # HTML comments
    ("<!-- Step 01: 模拟实例 -->", "<!-- Step 01: Simulation Instance -->"),
    ("<!-- 时间配置 -->", "<!-- Time Config -->"),
    ("<!-- 卡片头部 -->", "<!-- Card Header -->"),
    ("<!-- 活跃时间轴 -->", "<!-- Activity Timeline -->"),
    ("<!-- 行为参数 -->", "<!-- Behavior Params -->"),
    ("<!-- 平台配置 -->", "<!-- Platform Config -->"),
    ("<!-- 叙事方向 -->", "<!-- Narrative Direction -->"),
    ("<!-- 热点话题 -->", "<!-- Hot Topics -->"),
    ("<!-- 初始帖子流 -->", "<!-- Initial Posts -->"),
])

# ============================================================
# GraphPanel.vue - partial replacement & comments
# ============================================================
replace_in_file('frontend/src/components/GraphPanel.vue', [
    # Partial replacement fix
    ("还有少量内容处理中，建议稍后手动Обновить граф", "Обработка ещё не завершена, рекомендуется обновить граф позже"),
    # HTML comments
    ("<!-- 顶部工具栏 (Internal Top Right) -->", "<!-- Top Toolbar -->"),
    ("<!-- 图谱可视化 -->", "<!-- Graph Visualization -->"),
    ("<!-- 构建中/模拟中提示 -->", "<!-- Building/Simulating Hint -->"),
    ("<!-- 模拟结束后的提示 -->", "<!-- Post-Simulation Hint -->"),
    ("<!-- 节点/边详情面板 -->", "<!-- Node/Edge Detail Panel -->"),
    ("<!-- 节点详情 -->", "<!-- Node Details -->"),
])

# ============================================================
# Step5Interaction.vue - remaining visible text + comments
# ============================================================
replace_in_file('frontend/src/components/Step5Interaction.vue', [
    ("正在生成{{ section.title }}...", "Генерация {{ section.title }}..."),
    # Code comments (not user-visible but clean up)
    ("// 缓存所有对话记录", "// Cache all chat histories"),
    ("// 保存当前对话记录到缓存", "// Save current chat to cache"),
    ("// 保存当前对话记录", "// Save current chat"),
    ("// 恢复 Report Agent 的对话记录", "// Restore Report Agent chat"),
    ("// 恢复该 Agent 的对话记录", "// Restore this Agent's chat"),
])

# ============================================================
# HistoryDatabase.vue - HTML comments only
# ============================================================
replace_in_file('frontend/src/components/HistoryDatabase.vue', [
    ("<!-- 背景装饰：技术网格线（只在有项目时显示） -->", "<!-- Background Grid -->"),
    ("<!-- 标题区域 -->", "<!-- Title Area -->"),
    ("<!-- 卡片容器（只在有项目时显示） -->", "<!-- Cards Container -->"),
    ("<!-- 卡片头部：simulation_id 和 功能可用状态 -->", "<!-- Card Header -->"),
    ("<!-- 文件列表区域 -->", "<!-- File List Area -->"),
])

# ============================================================
# Process.vue - comments & remaining visible text
# ============================================================
replace_in_file('frontend/src/views/Process.vue', [
    ("title=\"刷新图谱\"", "title=\"Обновить граф\""),
    # HTML comments
    ("<!-- 顶部导航栏 -->", "<!-- Top Navbar -->"),
    ("<!-- 中间步骤指示器 -->", "<!-- Step Indicator -->"),
    ("<!-- 主内容区 -->", "<!-- Main Content -->"),
    ("<!-- 左侧: 实时图谱展示 -->", "<!-- Left: Real-time Graph -->"),
    ("<!-- 图谱可视化（只要有数据就显示） -->", "<!-- Graph Visualization -->"),
    ("<!-- 构建中提示 -->", "<!-- Building Hint -->"),
    ("<!-- узлов/边详情面板 -->", "<!-- Node/Edge Detail Panel -->"),
])

print("Fix pass done!")
