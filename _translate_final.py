"""
Final pass: translate ALL remaining Chinese text in frontend to Russian.
"""
import re, glob

replacements_by_file = {
    "frontend/src/views/Process.vue": [
        # Template visible text
        ("上传文档后，LLM分析文档内容，自动生成适合舆论模拟的本体结构（Типы сущностей + связей类型）",
         "После загрузки документов LLM анализирует содержание и автоматически генерирует онтологию (типы сущностей + типы связей)"),
        ("生成的связей类型", "Сгенерированные типы связей"),
        ("更多связей...", "ещё связей..."),
        ("基于生成的本体，将文档分块后调用 Zep API 构建知识图谱，提取实体和связей",
         "На основе сгенерированной онтологии документ разбивается на фрагменты, через Zep API строится граф знаний, извлекаются сущности и связи"),
        ("完成...", "Завершено..."),
        ("实体узлов", "Сущностей"),
        ("связей边", "Связей"),
        # JS strings
        ("Генерация онтологии进度", "Прогресс генерации онтологии"),
        ("Построение графа中", "Построение графа..."),
        ("Генерация онтологии中", "Генерация онтологии..."),
        ("Построение графа完成，正在加载完整数据...", "Построение графа завершено, загрузка данных..."),
        ("Построение завершено，正在加载图谱...", "Построение завершено, загрузка графа..."),
        ("Построение графа失败", "Ошибка построения графа"),
        ("Генерация онтологии失败", "Ошибка генерации онтологии"),
        ("处理失败", "Ошибка обработки"),
        ("正在启动Построение графа...", "Запуск построения графа..."),
        ("Построение графа任务已启动...", "Задача построения графа запущена..."),
        ("启动Построение графа失败", "Ошибка запуска построения графа"),
        ("未知错误", "неизвестная ошибка"),
        ("等待图谱数据...", "Ожидание данных графа..."),
        ("未命名", "Без имени"),
        ("保存原始数据", "// Save raw data"),
        ("未知", "Неизвестно"),
        ("加载完整图谱:", "Loading full graph:"),
        ("图谱加载完成", "Graph loaded"),
        ("进度", "progress"),
        ("上传中", "uploading"),
        ("选中的", "selected"),
        ("或边", "or edge"),
        ("阶段", "phase"),
        ("失败", "Ошибка"),
        ("正在启动", "Запуск..."),
        ("任务已启动", "Задача запущена"),
        ("启动失败", "Ошибка запуска"),
        ("完成正在加载完整数据", "Завершено, загрузка данных"),
        ("正在加载图谱", "Загрузка графа"),
        ("zh-CN", "ru-RU"),
        ("中", "..."),
    ],
    "frontend/src/views/MainView.vue": [
        ("图谱构建", "Построение графа"),
        ("环境搭建", "Настройка среды"),
        ("开始模拟", "Запуск симуляции"),
        ("报告生成", "Генерация отчёта"),
        ("深度互动", "Взаимодействие"),
    ],
    "frontend/src/views/SimulationRunView.vue": [
        ("默认每轮分钟", "// Default minutes per round"),
    ],
    "frontend/src/views/SimulationView.vue": [
        ("秒超时", "сек. таймаут"),
    ],
    "frontend/src/components/Step2EnvSetup.vue": [
        # Remaining partial Chinese
        ("若首次运行，强烈建议切换至'Настроить模式'减少模拟р数，以便快速预览效果并降低报错风险",
         "При первом запуске рекомендуем уменьшить количество раундов для быстрого предпросмотра"),
        ("初始化生成配置完成", "Инициализация, генерация, конфигурация, завершено"),
        ("默认使用自动配置数", "По умолчанию автоматическая настройка"),
        ("生成", "Генерация"),
        ("模拟数", "Раундов:"),
        ("模拟使用自动配置数", "Симуляция с автоматической настройкой раундов"),
        ("错误缺少", "Ошибка: отсутствует"),
        ("检测到已有完成的准备工作直接使用", "Обнаружена завершённая подготовка"),
        ("从图谱读取到实体", "Из графа извлечено сущностей:"),
        ("询准备进度", "Опрос прогресса подготовки"),
        ("准备失败未知错误", "Ошибка подготовки"),
        ("全部生成完成", "Все профили сгенерированы"),
        ("获取失败", "Ошибка загрузки"),
        ("正在生成配置", "Генерация конфигурации..."),
        ("正在调用参数", "Вызов LLM для генерации параметров..."),
        ("初始帖子条", "Начальных постов:"),
        ("时间配置每共", "Конфигурация времени:"),
        ("环境搭建完成可以模拟", "Среда готова, можно запускать симуляцию"),
        ("已加载", "Загружено:"),
        ("配置生成中询等待", "Конфигурация генерируется, ожидание..."),
    ],
    "frontend/src/components/Step3Simulation.vue": [
        ("从传入的最大轮数", "// Max rounds from parent"),
        ("默认每轮分钟", "// Default minutes per round"),
        ("未开始运行中已完成", "// not started, running, completed"),
        ("所有动作增量累积", "// All actions (incremental)"),
        ("用于去重的动作集合", "// Set for deduplication"),
        ("停止之前可能存在的轮询", "// Stop any existing polling"),
        ("强制重新开始", "// Force restart"),
        ("开启动态图谱更新", "// Enable dynamic graph update"),
        ("启动失败", "Ошибка запуска"),
        ("获取运行状态失败", "Ошибка получения статуса"),
        ("获取详细状态失败", "Ошибка получения деталей"),
    ],
    "frontend/src/components/Step4Report.vue": [
        # Tool icon descriptions (JS comments in object)
        ("灯泡图标代表洞察", "lightbulb - insight"),
        ("地球图标代表全景", "globe - panorama"),
        ("用户图标代表对话", "users - interview"),
        ("闪电图标代表快速", "zap - quick"),
        ("图表图标代表统计", "chart - statistics"),
        ("数据库图标代表实体", "database - entities"),
        # Regex parsing strings that match backend Chinese output
        ("分析问题", "分析问题"),  # Keep - matches backend
        ("预测场景", "Сценарий прогноза"),
        ("相关预测事实", "相关预测事实"),  # Keep - matches backend regex
        ("涉及实体", "涉及实体"),  # Keep - matches backend regex
        ("关系链", "关系链"),  # Keep - matches backend regex
        ("分析的子问题", "分析的子问题"),  # Keep - matches backend regex
        ("关键事实", "关键事实"),  # Keep - matches backend regex
        ("核心实体", "核心实体"),  # Keep - matches backend regex
        ("摘要", "摘要"),  # Keep - matches backend regex
        ("相关事实", "相关事实"),  # Keep - matches backend regex
        ("查询", "查询"),  # Keep - matches backend regex
        ("总节点数", "总节点数"),  # Keep - matches backend regex
        ("总边数", "总边数"),  # Keep - matches backend regex
        ("当前有效事实", "当前有效事实"),  # Keep - matches backend regex
        ("历史过期事实", "历史/过期事实"),  # Keep - matches backend regex
        ("当前有效事实", "当前有效事实"),  # Keep - matches backend regex
        ("采访主题", "采访主题"),  # Keep - matches backend regex
        ("采访人数", "采访人数"),  # Keep - matches backend regex
        ("采访对象采访实录", "采访对象选择理由"),  # Keep - matches backend regex
        ("选择", "选择"),  # Keep - matches backend regex
        ("未选综上最终选择", "未选|综上|最终选择"),  # Keep - matches backend regex
        ("采访", "采访"),  # Keep - matches backend regex
        ("简介", "简介"),  # Keep - matches backend regex
        ("关键引言", "关键引言"),  # Keep - matches backend regex
        ("平台回答平台回答", "平台回答"),  # Keep - matches backend regex
        ("平台回答", "平台回答"),  # Keep - matches backend regex
        ("采访摘要与核心观点", "采访摘要与核心观点"),  # Keep - matches backend regex
        ("搜索查询", "搜索查询"),  # Keep - matches backend regex
        ("找到条", "找到.*条"),  # Keep - matches backend regex
        ("相关边", "相关边"),  # Keep - matches backend regex
        ("相关节点", "相关节点"),  # Keep - matches backend regex
        # Visible UI labels in sub-components
        ("确保清除状态", "// Ensure state is cleared"),
        ("深灰色不随状态变化", "/* dark gray */"),
        # Visible text in InsightDisplay/PanoramaDisplay/etc sub-components
        ("Последние ключевые факты из временной памяти", "Последние ключевые факты из временной памяти"),
        ("共条", " шт."),
        ("收起展开全部条", "Свернуть / Развернуть"),
        ("共个", " шт."),
        ("收起展开全部个", "Свернуть / Развернуть"),
        ("暂无", "Нет данных"),
        ("漂移查询生成分析", "Drift-запрос: подвопросы"),
        ("无回复", "Нет ответа"),
        ("条", " шт."),
        ("Вопрос", "Вопрос"),
        ("结果", "Результаты"),
        ("Мир", "Мир"),
    ],
    "frontend/src/components/Step5Interaction.vue": [
        ("向发送", "Отправка:"),
        ("给个对象", "объектов"),
        ("加载报告", "Загрузка отчёта"),
        ("报告加载完成", "Отчёт загружен"),
        ("加载了个模拟个体", "Загружено агентов:"),
    ],
    "frontend/src/components/GraphPanel.vue": [
        ("已处理过跳过", "// Already processed, skip"),
        ("基础每多一条边增加", "// Base + increment per edge"),
        ("保持水平", "// Keep horizontal"),
    ],
    "frontend/src/components/HistoryDatabase.vue": [
        ("开始模拟与深度互动", "Начать симуляцию и взаимодействие"),
        ("当前选中的项目用于弹窗", "// Selected project for modal"),
        ("动画锁防止闪烁", "// Animation lock"),
        ("已完成", "/* completed */"),
        ("进行中", "/* in progress */"),
    ],
}

def process():
    changed = []
    for filepath, repls in replacements_by_file.items():
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            continue
        
        original = content
        for old, new in repls:
            if old == new:
                continue  # Skip no-ops (backend regex matches we keep)
            if old in content:
                content = content.replace(old, new)
                print(f"  {filepath}: '{old[:50]}' -> '{new[:50]}'")
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            changed.append(filepath)
    
    print(f"\nChanged {len(changed)} files")
    
    # Final check
    print("\n=== Remaining Chinese [TEXT] (non-comment) ===")
    chinese = re.compile(r'[\u4e00-\u9fff]+')
    count = 0
    for f in sorted(glob.glob("frontend/src/**/*.vue", recursive=True) + glob.glob("frontend/src/**/*.js", recursive=True)):
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                for i, line in enumerate(fh, 1):
                    if chinese.search(line):
                        s = line.strip()
                        if not (s.startswith('//') or s.startswith('/*') or s.startswith('*') or s.startswith('<!--')):
                            matches = chinese.findall(line)
                            text = ''.join(matches)
                            # Skip if it's only in a comment part of the line
                            if '//' in s:
                                before_comment = s[:s.index('//')]
                                if not chinese.search(before_comment):
                                    continue
                            print(f"  {f}:{i} {text}")
                            count += 1
        except:
            pass
    print(f"\nTotal remaining: {count}")

process()
