# -*- coding: utf-8 -*-
"""Translate remaining JS comments in Home.vue."""

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

replace_in_file('frontend/src/views/Home.vue', [
    ("// 处理文件选择", "// Handle file select"),
    ("// 处理拖拽相关", "// Handle drag events"),
    ("// 添加文件", "// Add files"),
    ("// 移除文件", "// Remove file"),
    ("// 滚动到底部", "// Scroll to bottom"),
    ("// 开始模拟 - 立即跳转，API调用在Process页面进行", "// Start simulation - redirect to Process page"),
    ("// 存储待上传的数据", "// Store pending upload data"),
    ("// 立即跳转到Process页面（使用特殊标识表示新建项目）", "// Redirect to Process page (new project)"),
])

print("Done!")
