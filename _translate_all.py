# -*- coding: utf-8 -*-
"""Translate all Chinese UI strings to Russian across MiroFish frontend."""

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
    return count

# ============================================================
# MainView.vue
# ============================================================
replace_in_file('frontend/src/views/MainView.vue', [
    ("graph: '图谱', split: '双栏', workbench: '工作台'", "graph: 'Граф', split: 'Сплит', workbench: 'Панель'"),
    ("const stepNames = ['图谱构建', '环境搭建', '开始模拟', '报告生成', '深度互动']",
     "const stepNames = ['Построение графа', 'Настройка среды', 'Запуск симуляции', 'Генерация отчёта', 'Глубокое взаимодействие']"),
    ("addLog(`进入 Step ${currentStep.value}: ${stepNames[currentStep.value - 1]}`)", "addLog(`Переход к Step ${currentStep.value}: ${stepNames[currentStep.value - 1]}`)"),
    ("addLog(`自定义模拟轮数: ${params.maxRounds} 轮`)", "addLog(`Пользовательское кол-во раундов: ${params.maxRounds}`)"),
    ("addLog(`返回 Step ${currentStep.value}: ${stepNames[currentStep.value - 1]}`)", "addLog(`Возврат к Step ${currentStep.value}: ${stepNames[currentStep.value - 1]}`)"),
])

# ============================================================
# SimulationView.vue (Step 2 wrapper)
# ============================================================
replace_in_file('frontend/src/views/SimulationView.vue', [
    ("graph: '图谱', split: '双栏', workbench: '工作台'", "graph: 'Граф', split: 'Сплит', workbench: 'Панель'"),
    ("<span class=\"step-name\">环境搭建</span>", "<span class=\"step-name\">Настройка среды</span>"),
    ("addLog('进入 Step 3: 开始模拟')", "addLog('Переход к Step 3: Запуск симуляции')"),
    ("addLog(`自定义模拟轮数: ${params.maxRounds} 轮`)", "addLog(`Пользовательское кол-во раундов: ${params.maxRounds}`)"),
    ("addLog('使用自动配置的模拟轮数')", "addLog('Используются автоматические настройки раундов')"),
    ("addLog(`加载模拟数据: ${currentSimulationId.value}`)", "addLog(`Загрузка данных симуляции: ${currentSimulationId.value}`)"),
    ("addLog(`项目加载成功: ${projRes.data.project_id}`)", "addLog(`Проект загружен: ${projRes.data.project_id}`)"),
    ("addLog('图谱数据加载成功')", "addLog('Данные графа загружены')"),
    ("addLog(`图谱加载失败: ${err.message}`)", "addLog(`Ошибка загрузки графа: ${err.message}`)"),
    ("addLog('SimulationView 初始化')", "addLog('SimulationView инициализация')"),
    ("addLog('检测到模拟环境正在运行，正在关闭...')", "addLog('Обнаружена работающая симуляция, закрытие...')"),
    ("addLog('✓ 模拟环境已关闭')", "addLog('✓ Среда симуляции закрыта')"),
    ("addLog(`关闭模拟环境失败: ${closeRes.error || '未知错误'}`)", "addLog(`Ошибка закрытия среды: ${closeRes.error || 'неизвестная ошибка'}`)"),
    ("addLog(`关闭模拟环境异常: ${closeErr.message}`)", "addLog(`Исключение при закрытии среды: ${closeErr.message}`)"),
    ("addLog('检测到模拟状态为运行中，正在停止...')", "addLog('Обнаружена активная симуляция, остановка...')"),
    ("addLog('✓ 模拟已强制停止')", "addLog('✓ Симуляция принудительно остановлена')"),
    ("addLog(`强制停止模拟失败: ${stopRes.error || '未知错误'}`)", "addLog(`Ошибка принудительной остановки: ${stopRes.error || 'неизвестная ошибка'}`)"),
    ("addLog(`强制停止模拟异常: ${err.message}`)", "addLog(`Исключение при остановке: ${err.message}`)"),
    ("addLog(`加载模拟数据失败: ${simRes.error || '未知错误'}`)", "addLog(`Ошибка загрузки данных: ${simRes.error || 'неизвестная ошибка'}`)"),
    ("addLog(`加载异常: ${err.message}`)", "addLog(`Ошибка загрузки: ${err.message}`)"),
])

# ============================================================
# SimulationRunView.vue (Step 3 wrapper)
# ============================================================
replace_in_file('frontend/src/views/SimulationRunView.vue', [
    ("graph: '图谱', split: '双栏', workbench: '工作台'", "graph: 'Граф', split: 'Сплит', workbench: 'Панель'"),
    ("<span class=\"step-name\">开始模拟</span>", "<span class=\"step-name\">Запуск симуляции</span>"),
    ("addLog('SimulationRunView 初始化')", "addLog('SimulationRunView инициализация')"),
    ("addLog(`自定义模拟轮数: ${maxRounds.value}`)", "addLog(`Пользовательское кол-во раундов: ${maxRounds.value}`)"),
    ("addLog(`加载模拟数据: ${currentSimulationId.value}`)", "addLog(`Загрузка данных симуляции: ${currentSimulationId.value}`)"),
    ("addLog(`时间配置: 每轮 ${minutesPerRound.value} 分钟`)", "addLog(`Настройка времени: ${minutesPerRound.value} мин/раунд`)"),
    ("addLog(`获取时间配置失败，使用默认值: ${minutesPerRound.value}分钟/轮`)", "addLog(`Ошибка получения настроек, по умолчанию: ${minutesPerRound.value} мин/раунд`)"),
    ("addLog(`项目加载成功: ${projRes.data.project_id}`)", "addLog(`Проект загружен: ${projRes.data.project_id}`)"),
    ("addLog('图谱数据加载成功')", "addLog('Данные графа загружены')"),
    ("addLog(`图谱加载失败: ${err.message}`)", "addLog(`Ошибка загрузки графа: ${err.message}`)"),
    ("addLog(`加载模拟数据失败: ${simRes.error || '未知错误'}`)", "addLog(`Ошибка загрузки данных: ${simRes.error || 'неизвестная ошибка'}`)"),
    ("addLog(`加载异常: ${err.message}`)", "addLog(`Ошибка загрузки: ${err.message}`)"),
    ("addLog('准备返回 Step 2，正在关闭模拟...')", "addLog('Возврат к Step 2, закрытие симуляции...')"),
    ("addLog('正在关闭模拟环境...')", "addLog('Закрытие среды симуляции...')"),
    ("addLog('✓ 模拟环境已关闭')", "addLog('✓ Среда симуляции закрыта')"),
    ("addLog(`关闭模拟环境失败，尝试强制停止...`)", "addLog(`Ошибка закрытия среды, принудительная остановка...`)"),
    ("addLog('✓ 模拟已强制停止')", "addLog('✓ Симуляция принудительно остановлена')"),
    ("addLog(`强制停止失败: ${stopErr.message}`)", "addLog(`Ошибка принудительной остановки: ${stopErr.message}`)"),
    ("addLog('正在停止模拟进程...')", "addLog('Остановка процесса симуляции...')"),
    ("addLog('✓ 模拟已停止')", "addLog('✓ Симуляция остановлена')"),
    ("addLog(`停止模拟失败: ${err.message}`)", "addLog(`Ошибка остановки: ${err.message}`)"),
    ("addLog(`检查模拟状态失败: ${err.message}`)", "addLog(`Ошибка проверки статуса: ${err.message}`)"),
    ("addLog('进入 Step 4: 报告生成')", "addLog('Переход к Step 4: Генерация отчёта')"),
    ("addLog('开启图谱实时刷新 (30s)')", "addLog('Автообновление графа включено (30с)')"),
    ("addLog('停止图谱实时刷新')", "addLog('Автообновление графа остановлено')"),
])

# ============================================================
# ReportView.vue (Step 4 wrapper)
# ============================================================
replace_in_file('frontend/src/views/ReportView.vue', [
    ("graph: '图谱', split: '双栏', workbench: '工作台'", "graph: 'Граф', split: 'Сплит', workbench: 'Панель'"),
    ("<span class=\"step-name\">报告生成</span>", "<span class=\"step-name\">Генерация отчёта</span>"),
    ("addLog('ReportView 初始化')", "addLog('ReportView инициализация')"),
    ("addLog(`加载报告数据: ${currentReportId.value}`)", "addLog(`Загрузка данных отчёта: ${currentReportId.value}`)"),
    ("addLog(`项目加载成功: ${projRes.data.project_id}`)", "addLog(`Проект загружен: ${projRes.data.project_id}`)"),
    ("addLog('图谱数据加载成功')", "addLog('Данные графа загружены')"),
    ("addLog(`图谱加载失败: ${err.message}`)", "addLog(`Ошибка загрузки графа: ${err.message}`)"),
    ("addLog(`获取报告信息失败: ${reportRes.error || '未知错误'}`)", "addLog(`Ошибка получения отчёта: ${reportRes.error || 'неизвестная ошибка'}`)"),
    ("addLog(`加载异常: ${err.message}`)", "addLog(`Ошибка загрузки: ${err.message}`)"),
])

# ============================================================
# InteractionView.vue (Step 5 wrapper)
# ============================================================
replace_in_file('frontend/src/views/InteractionView.vue', [
    ("graph: '图谱', split: '双栏', workbench: '工作台'", "graph: 'Граф', split: 'Сплит', workbench: 'Панель'"),
    ("<span class=\"step-name\">深度互动</span>", "<span class=\"step-name\">Глубокое взаимодействие</span>"),
    ("addLog('InteractionView 初始化')", "addLog('InteractionView инициализация')"),
    ("addLog(`加载报告数据: ${currentReportId.value}`)", "addLog(`Загрузка данных отчёта: ${currentReportId.value}`)"),
    ("addLog(`项目加载成功: ${projRes.data.project_id}`)", "addLog(`Проект загружен: ${projRes.data.project_id}`)"),
    ("addLog('图谱数据加载成功')", "addLog('Данные графа загружены')"),
    ("addLog(`图谱加载失败: ${err.message}`)", "addLog(`Ошибка загрузки графа: ${err.message}`)"),
    ("addLog(`获取报告信息失败: ${reportRes.error || '未知错误'}`)", "addLog(`Ошибка получения отчёта: ${reportRes.error || 'неизвестная ошибка'}`)"),
    ("addLog(`加载异常: ${err.message}`)", "addLog(`Ошибка загрузки: ${err.message}`)"),
])

# ============================================================
# Step1GraphBuild.vue
# ============================================================
replace_in_file('frontend/src/components/Step1GraphBuild.vue', [
    ("<span class=\"step-title\">本体生成</span>", "<span class=\"step-title\">Генерация онтологии</span>"),
    ("<span v-if=\"currentPhase > 0\" class=\"badge success\">已完成</span>", "<span v-if=\"currentPhase > 0\" class=\"badge success\">Готово</span>"),
    ("<span v-else-if=\"currentPhase === 0\" class=\"badge processing\">生成中</span>", "<span v-else-if=\"currentPhase === 0\" class=\"badge processing\">Генерация</span>"),
    ("<span v-else class=\"badge pending\">等待</span>", "<span v-else class=\"badge pending\">Ожидание</span>"),
    ("LLM分析文档内容与模拟需求，提取出现实种子，自动生成合适的本体结构", "LLM анализирует документы и требования, извлекает реальные зёрна и генерирует структуру онтологии"),
    ("ontologyProgress.message || '正在分析文档...'", "ontologyProgress.message || 'Анализ документов...'"),
    ("<span class=\"step-title\">GraphRAG构建</span>", "<span class=\"step-title\">Построение GraphRAG</span>"),
    ("<span v-if=\"currentPhase > 1\" class=\"badge success\">已完成</span>", "<span v-if=\"currentPhase > 1\" class=\"badge success\">Готово</span>"),
    ("基于生成的本体，将文档自动分块后调用 Zep 构建知识图谱，提取实体和关系，并形成时序记忆与社区摘要",
     "На основе онтологии документы разбиваются на блоки, через Zep строится граф знаний с извлечением сущностей и связей"),
    ("<span class=\"stat-label\">实体节点</span>", "<span class=\"stat-label\">Узлы сущностей</span>"),
    ("<span class=\"stat-label\">关系边</span>", "<span class=\"stat-label\">Рёбра связей</span>"),
    ("<span class=\"stat-label\">SCHEMA类型</span>", "<span class=\"stat-label\">Типы схемы</span>"),
    ("<span class=\"step-title\">构建完成</span>", "<span class=\"step-title\">Построение завершено</span>"),
    ("<span v-if=\"currentPhase >= 2\" class=\"badge accent\">进行中</span>", "<span v-if=\"currentPhase >= 2\" class=\"badge accent\">В процессе</span>"),
    ("图谱构建已完成，请进入下一步进行模拟环境搭建", "Граф построен. Перейдите к следующему шагу для настройки среды симуляции"),
    ("creatingSimulation ? '创建中...' : '进入环境搭建 ➝'", "creatingSimulation ? 'Создание...' : 'Настройка среды ➝'"),
    ("console.error('缺少项目或图谱信息')", "console.error('Отсутствуют данные проекта или графа')"),
    ("console.error('创建模拟失败:', res.error)", "console.error('Ошибка создания симуляции:', res.error)"),
    ("alert('创建模拟失败: ' + (res.error || '未知错误'))", "alert('Ошибка создания симуляции: ' + (res.error || 'неизвестная ошибка'))"),
    ("console.error('创建模拟异常:', err)", "console.error('Исключение при создании симуляции:', err)"),
    ("alert('创建模拟异常: ' + err.message)", "alert('Ошибка создания симуляции: ' + err.message)"),
])

print("All view/step1 translations done!")
