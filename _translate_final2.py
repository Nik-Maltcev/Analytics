"""
Final pass 2: fix remaining partial Chinese text by reading exact lines.
"""
import re

def fix_file(filepath, line_replacements):
    """Replace text on specific lines."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    changed = False
    for line_num, old, new in line_replacements:
        idx = line_num - 1
        if idx < len(lines) and old in lines[idx]:
            lines[idx] = lines[idx].replace(old, new)
            print(f"  {filepath}:{line_num} OK")
            changed = True
        else:
            # Try nearby lines (±3)
            for offset in range(-3, 4):
                check_idx = idx + offset
                if 0 <= check_idx < len(lines) and old in lines[check_idx]:
                    lines[check_idx] = lines[check_idx].replace(old, new)
                    print(f"  {filepath}:{check_idx+1} OK (offset {offset})")
                    changed = True
                    break
            else:
                print(f"  {filepath}:{line_num} NOT FOUND: '{old[:40]}'")
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    return changed


# HistoryDatabase remaining
fix_file("frontend/src/components/HistoryDatabase.vue", [
    (184, "开始模拟与深度互动", "Начать симуляцию"),
])

# Step2 remaining - need to read exact lines
fix_file("frontend/src/components/Step2EnvSetup.vue", [
    (504, "若首次运行", "При первом запуске рекомендуем уменьшить количество раундов"),
    (504, "强烈建议切换至", ""),
    (504, "模式减少模拟", ""),
    (504, "数以便快速预览效果并降低报错风险", ""),
    (748, "模拟数", "Раундов:"),
    (751, "模拟使用自动配置数", "Симуляция с автонастройкой раундов"),
    (771, "错误缺少", "Ошибка: отсутствует"),
    (791, "检测到已有完成的准备工作直接使用", "Обнаружена завершённая подготовка"),
    (803, "从图谱读取到实体", "Из графа извлечено сущностей:"),
    (815, "准备失败未知错误", "Ошибка подготовки"),
    (898, "准备失败未知错误", "Ошибка подготовки"),
    (943, "全部完成", "Все сгенерированы"),
    (948, "获取失败", "Ошибка загрузки"),
    (977, "正在配置", "Генерация конфигурации..."),
    (979, "正在调用参数", "Вызов LLM..."),
    (992, "初始帖子条", "Начальных постов:"),
    (1000, "时间配置每共", "Конфигурация времени:"),
    (1011, "环境搭建完成可以模拟", "Среда готова"),
    (1016, "获取失败", "Ошибка загрузки"),
    (1040, "初始帖子条", "Начальных постов:"),
    (1043, "环境搭建完成可以模拟", "Среда готова"),
    (1048, "配置中询等待", "Конфигурация генерируется..."),
    (654, "初始化", "Инициализация"),
    (654, "配置完成", "конфигурация завершена"),
    (672, "默认使用自动配置数", "По умолчанию автонастройка"),
])

# Step5 remaining
fix_file("frontend/src/components/Step5Interaction.vue", [
    (714, "向发送", "Отправка:"),
    (806, "给个对象", "объектов"),
    (907, "报告加载完成", "Отчёт загружен"),
    (921, "加载了个模拟个体", "Загружено агентов:"),
])

# Step4 - visible UI text (not regex parsing)
fix_file("frontend/src/components/Step4Report.vue", [
    (2459, "深灰色不随状态变化", "/* dark gray */"),
    (1045, "共", "всего"),
    (1058, "收起展开全部", "Свернуть / Развернуть"),
    (1065, "共个", "всего"),
    (1079, "收起展开全部个", "Свернуть / Развернуть"),
    (1086, "共", "всего"),
    (1104, "收起展开全部", "Свернуть / Развернуть"),
    (1111, "共个", "всего"),
    (1201, "共", "всего"),
    (1214, "收起展开全部", "Свернуть / Развернуть"),
    (1221, "共", "всего"),
    (1246, "收起展开全部", "Свернуть / Развернуть"),
    (1253, "共个", "всего"),
    (1266, "收起展开全部个", "Свернуть / Развернуть"),
    (1646, "共", "всего"),
    (1659, "收起展开全部", "Свернуть / Развернуть"),
    (1665, "相关", "Связанные"),
    (1666, "共", "всего"),
    (1686, "相关", "Связанные"),
    (1687, "共个", "всего"),
])

# Process.vue remaining
fix_file("frontend/src/views/Process.vue", [
    (700, "启动", "Ошибка запуска"),
    (705, "启动", "Ошибка запуска"),
])

# Final count
print("\n=== Final remaining Chinese [TEXT] ===")
chinese = re.compile(r'[\u4e00-\u9fff]+')
import glob
count = 0
for f in sorted(glob.glob("frontend/src/**/*.vue", recursive=True) + glob.glob("frontend/src/**/*.js", recursive=True)):
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            for i, line in enumerate(fh, 1):
                if chinese.search(line):
                    s = line.strip()
                    if not (s.startswith('//') or s.startswith('/*') or s.startswith('*') or s.startswith('<!--')):
                        if '//' in s:
                            before = s[:s.index('//')]
                            if not chinese.search(before):
                                continue
                        matches = chinese.findall(line)
                        print(f"  {f}:{i} {''.join(matches)}")
                        count += 1
    except:
        pass
print(f"\nTotal remaining: {count}")
