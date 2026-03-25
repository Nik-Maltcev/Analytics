"""Translate remaining English strings."""

def fix(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Fixed {filepath}")

fix("frontend/src/views/InteractionView.vue", [
    ("return 'Processing'", "return 'Обработка'"),
    ("return 'Ready'", "return 'Готово'"),
])

fix("frontend/src/views/MainView.vue", [
    ("return 'Initializing'", "return 'Инициализация'"),
    ("'Project view initialized.'", "'Инициализация проекта.'"),
    ("'Error: No pending files found for new project.'", "'Ошибка: нет файлов для загрузки.'"),
    ("'Graph data loaded successfully.'", "'Данные графа загружены.'"),
    ("'Manual graph refresh triggered.'", "'Обновление графа.'"),
    ("'Graph polling stopped.'", "'Опрос графа остановлен.'"),
])

fix("frontend/src/views/Process.vue", [
    ("'Error'", "'Ошибка'"),
    ("'Ready'", "'Готово'"),
    ("'Preparing'", "'Подготовка'"),
])

print("Done!")
