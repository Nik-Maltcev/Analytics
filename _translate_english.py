"""Translate remaining English user-visible strings to Russian."""

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"  {filepath}: '{old[:50]}' -> '{new[:50]}'")
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# MainView.vue
replace_in_file("frontend/src/views/MainView.vue", [
    ("'Error'", "'Ошибка'"),
    ("'Ready'", "'Готово'"),
    ("'Building Graph'", "'Построение графа'"),
    ("'Generating Ontology'", "'Генерация онтологии'"),
    ("'Uploading and analyzing docs...'", "'Загрузка и анализ документов...'"),
    ("'Starting ontology generation: Uploading files...'", "'Генерация онтологии: загрузка файлов...'"),
    ("'Starting build...'", "'Запуск построения...'"),
    ("'Initiating graph build...'", "'Запуск построения графа...'"),
    ("'Started polling for graph data...'", "'Начат опрос данных графа...'"),
    ("'Graph build task completed.'", "'Построение графа завершено.'"),
    ("'Preparing'", "'Подготовка'"),
])

# SimulationView.vue
replace_in_file("frontend/src/views/SimulationView.vue", [
    ("'Error'", "'Ошибка'"),
    ("'Ready'", "'Готово'"),
    ("'Preparing'", "'Подготовка'"),
])

# SimulationRunView.vue
replace_in_file("frontend/src/views/SimulationRunView.vue", [
    ("'Error'", "'Ошибка'"),
    ("'Completed'", "'Завершено'"),
    ("'Running'", "'Выполняется'"),
])

# ReportView.vue
replace_in_file("frontend/src/views/ReportView.vue", [
    ("'Error'", "'Ошибка'"),
    ("'Completed'", "'Завершено'"),
    ("'Generating'", "'Генерация'"),
])

# InteractionView.vue
replace_in_file("frontend/src/views/InteractionView.vue", [
    ("'Error'", "'Ошибка'"),
    ("'Completed'", "'Завершено'"),
    ("'Loading'", "'Загрузка'"),
])

# Now scan all vue files for remaining English visible text
import re, glob

# Common English UI patterns to find
patterns = [
    r"'[A-Z][a-z]+(?:\s[a-z]+)*\.\.\.'",  # 'Loading...' etc
    r"'[A-Z][a-z]+(?:\s[A-Za-z]+)*'",  # Status text like 'Ready'
]

print("\n=== Remaining English status/UI text ===")
# Check specific known patterns
for f in sorted(glob.glob("frontend/src/views/*.vue")):
    with open(f, 'r', encoding='utf-8') as fh:
        for i, line in enumerate(fh, 1):
            s = line.strip()
            # Look for statusText computed or addLog with English
            if ('statusText' in s or 'return ' in s) and re.search(r"return\s+'[A-Z]", s):
                print(f"  {f}:{i} {s[:80]}")
            if 'addLog(' in s and re.search(r"'[A-Z][a-z]", s):
                print(f"  {f}:{i} {s[:80]}")
            if '.message' in s and re.search(r"'[A-Z][a-z]", s):
                print(f"  {f}:{i} {s[:80]}")

print("\nDone!")
