# -*- coding: utf-8 -*-
"""Translate remaining comments in Home.vue."""

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
    ("<!-- 上传区域 -->", "<!-- Upload Area -->"),
    ("<!-- 分割线 -->", "<!-- Divider -->"),
    ("<!-- 输入区域 -->", "<!-- Input Area -->"),
    ("<!-- 启动按钮 -->", "<!-- Start Button -->"),
    ("<!-- 历史项目数据库 -->", "<!-- History Database -->"),
    ("// 表单数据", "// Form data"),
    ("// 文件列表", "// File list"),
    ("// 状态", "// State"),
    ("// 文件输入引用", "// File input ref"),
    ("// 计算属性:是否可以提交", "// Computed: can submit"),
    ("// 触发文件选择", "// Trigger file select"),
])

print("Done!")
