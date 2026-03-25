"""
Final pass 3: Replace ALL remaining Chinese characters in frontend with Russian.
Uses regex to find and replace Chinese text in context.
"""
import re, glob

chinese_re = re.compile(r'[\u4e00-\u9fff，。！？；：""''【】（）]+')

# Map of Chinese text fragments to Russian replacements
# These will be applied as regex replacements
fragment_map = {
    # Step2EnvSetup.vue - line 504 (the stubborn one)
    "模式'减少模拟р数，以便快速预览效果并降低报错风险": "",
    "，'Настроить": " и переключиться в режим 'Настроить'",
    
    # Step2 JS strings  
    "模拟р数": "раундов",
    "模拟使用自动配置数": "Симуляция с автонастройкой",
    "错误缺少": "Ошибка: отсутствует",
    "检测到已有完成的准备工作直接使用": "Обнаружена завершённая подготовка",
    "从图谱读取到实体": "Из графа извлечено сущностей:",
    "准备失败未知错误": "Ошибка подготовки",
    "全部完成": "Все сгенерированы",
    "获取失败": "Ошибка загрузки",
    "正在配置": "Генерация конфигурации",
    "正在调用参数": "Вызов LLM",
    "初始帖子条": "Начальных постов:",
    "时间配置每共": "Конфигурация времени:",
    "环境搭建完成可以模拟": "Среда готова",
    "配置中询等待": "Конфигурация генерируется...",
    "初始化": "Инициализация",
    "配置完成": "конфигурация завершена",
    "默认使用自动配置数": "По умолчанию автонастройка",
    
    # HistoryDatabase
    "开始模拟与深度互动": "Начать симуляцию",
    
    # Step4Report - visible UI text in sub-components
    "收起展开全部个": "Свернуть / Развернуть",
    "收起展开全部": "Свернуть / Развернуть",
    "共个": " всего",
    "共": " всего ",
    "深灰色不随状态变化": "/* dark gray */",
    
    # Step4Report - regex parsing strings (match backend Chinese output - KEEP but these are in JS regex)
    # These are used in regex patterns to parse backend response, they MUST stay Chinese
    # to match the backend output. But they show up as "remaining" - that's OK.
    
    # Step5Interaction
    "向发送": "Отправка:",
    "给个对象": "объектов",
    "报告加载完成": "Отчёт загружен",
    "加载了个模拟个体": "Загружено агентов:",
    
    # Process.vue
    "启动": "Запуск",
}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Sort by length descending to replace longer matches first
    sorted_frags = sorted(fragment_map.items(), key=lambda x: len(x[0]), reverse=True)
    
    for old, new in sorted_frags:
        if old in content:
            content = content.replace(old, new)
            print(f"  {filepath}: '{old[:40]}' -> '{new[:40]}'")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Process all frontend files
changed = []
for f in sorted(glob.glob("frontend/src/**/*.vue", recursive=True) + glob.glob("frontend/src/**/*.js", recursive=True)):
    if process_file(f):
        changed.append(f)

print(f"\nChanged {len(changed)} files")

# Final count
print("\n=== Final remaining Chinese [TEXT] ===")
count = 0
for f in sorted(glob.glob("frontend/src/**/*.vue", recursive=True) + glob.glob("frontend/src/**/*.js", recursive=True)):
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            for i, line in enumerate(fh, 1):
                if chinese_re.search(line):
                    s = line.strip()
                    # Skip pure comments
                    if s.startswith('//') or s.startswith('/*') or s.startswith('*') or s.startswith('<!--'):
                        continue
                    # Skip if Chinese is only in comment part
                    if '//' in s:
                        before = s[:s.index('//')]
                        if not chinese_re.search(before):
                            continue
                    matches = chinese_re.findall(line)
                    text = ''.join(matches)
                    print(f"  {f}:{i} {text}")
                    count += 1
    except:
        pass
print(f"\nTotal remaining: {count}")
