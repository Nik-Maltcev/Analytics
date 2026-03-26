"""Translate ReportLogger messages and hide console logs in Step4/Step5."""

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
    else:
        print(f"  No changes in {filepath}")

# 1. ReportLogger messages in report_agent.py
fix("backend/app/services/report_agent.py", [
    ('"报告生成任务开始"', '"Начало генерации отчёта"'),
    ('"开始规划报告大纲"', '"Начало планирования структуры отчёта"'),
    ('"获取模拟上下文信息"', '"Получение контекста симуляции"'),
    ('"大纲规划完成"', '"Планирование структуры завершено"'),
    ('f"开始生成章节: {section_title}"', 'f"Начало генерации раздела: {section_title}"'),
    ('f"ReACT 第{iteration}轮思考"', 'f"ReACT итерация {iteration}"'),
    ('f"调用工具: {tool_name}"', 'f"Вызов инструмента: {tool_name}"'),
    ('f"工具 {tool_name} 返回结果"', 'f"Инструмент {tool_name} вернул результат"'),
    ('f"LLM 响应 (工具调用: {has_tool_calls}, 最终答案: {has_final_answer})"',
     'f"LLM ответ (инструменты: {has_tool_calls}, финальный ответ: {has_final_answer})"'),
    ('f"章节 {section_title} 内容生成完成"', 'f"Раздел {section_title} — контент сгенерирован"'),
    ('f"章节 {section_title} 生成完成"', 'f"Раздел {section_title} завершён"'),
    ('"报告生成完成"', '"Генерация отчёта завершена"'),
    ('f"发生错误: {error_message}"', 'f"Ошибка: {error_message}"'),
    # Logger messages
    ('"开始规划报告大纲..."', '"Планирование структуры отчёта..."'),
    ('"大纲规划完成"', '"Структура отчёта готова"'),
    ('f"大纲规划完成: {len(sections)} 个章节"', 'f"Структура готова: {len(sections)} разделов"'),
    ('f"大纲规划失败: {str(e)}"', 'f"Ошибка планирования: {str(e)}"'),
    ('f"章节 {section.title} 生成完成（工具调用: {tool_calls_count}次）"',
     'f"Раздел {section.title} завершён (вызовов инструментов: {tool_calls_count})"'),
    ('f"章节 {section.title} 达到最大迭代次数，强制生成"',
     'f"Раздел {section.title}: достигнут лимит итераций, принудительная генерация"'),
    ('f"（本章节生成失败：LLM 返回空响应，请稍后重试）"',
     'f"(Ошибка генерации раздела: LLM вернул пустой ответ, попробуйте позже)"'),
    ('"（响应为空）"', '"(пустой ответ)"'),
    ('"请继续生成内容。"', '"Продолжайте генерацию контента."'),
    # Progress messages
    ('"开始规划报告大纲..."', '"Планирование структуры отчёта..."'),
    ('f"大纲规划完成，共{len(outline.sections)}个章节"', 'f"Структура готова: {len(outline.sections)} разделов"'),
    ('"报告生成完成"', '"Генерация отчёта завершена"'),
    ('f"报告生成完成: {report_id}"', 'f"Отчёт сгенерирован: {report_id}"'),
    ('f"报告生成失败: {str(e)}"', 'f"Ошибка генерации отчёта: {str(e)}"'),
])

# 2. Hide console logs in Step4Report.vue and Step5Interaction.vue
for filepath in ["frontend/src/components/Step4Report.vue"]:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old = """    <!-- Bottom Console Logs -->
    <div class="console-logs">
      <div class="log-header">
        <span class="log-title">CONSOLE OUTPUT</span>
        <span class="log-id">{{ reportId || 'NO_REPORT' }}</span>
      </div>
      <div class="log-content" ref="logContent">
        <div class="log-line" v-for="(log, idx) in consoleLogs" :key="idx">
          <span class="log-msg" :class="getLogLevelClass(log)">{{ log }}</span>
        </div>
      </div>
    </div>"""
    
    new = """    <!-- Bottom Console Logs (hidden) -->
    <!--
    <div class="console-logs">
      <div class="log-header">
        <span class="log-title">CONSOLE OUTPUT</span>
        <span class="log-id">{{ reportId || 'NO_REPORT' }}</span>
      </div>
      <div class="log-content" ref="logContent">
        <div class="log-line" v-for="(log, idx) in consoleLogs" :key="idx">
          <span class="log-msg" :class="getLogLevelClass(log)">{{ log }}</span>
        </div>
      </div>
    </div>
    -->"""
    
    if old in content:
        content = content.replace(old, new)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Hidden console logs in {filepath}")
    else:
        print(f"  Console logs not found in {filepath}")

print("\n✅ Done!")
