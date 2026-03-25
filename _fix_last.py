"""Fix last remaining issues."""

# Fix Step2 line 943
with open("frontend/src/components/Step2EnvSetup.vue", 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace("全部 ${currentCount} профилей агентов сгенерировано", "Все ${currentCount} профилей агентов сгенерированы")
with open("frontend/src/components/Step2EnvSetup.vue", 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed Step2")

# Fix remaining broken regex in Step4 (partially translated)
with open("frontend/src/components/Step4Report.vue", 'r', encoding='utf-8') as f:
    content = f.read()

# These were partially translated - restore to match backend output
fixes = [
    ("相关预测Факты:", "相关预测事实:"),
    ("关键Факты", "关键事实"),
    ("当前有效Факты", "当前有效事实"),
    ("采访对象Причина выбора", "采访对象选择理由"),
]
for old, new in fixes:
    if old in content:
        content = content.replace(old, new)
        print(f"Fixed regex: {old} -> {new}")

with open("frontend/src/components/Step4Report.vue", 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed Step4")
