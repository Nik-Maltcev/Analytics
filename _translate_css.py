# -*- coding: utf-8 -*-
"""Translate CSS and remaining comments."""

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
    ("/* 全局变量与重置 */", "/* Global vars & reset */"),
    ("使用 Space Grotesk 作为主要标题字体，JetBrains Mono 作为代码/标签字体", "Space Grotesk for headings, JetBrains Mono for code"),
    ("确保已在 index.html 引入这些 Google Fonts", "Ensure Google Fonts are imported in index.html"),
    ("/* 顶部导航 */", "/* Top Navbar */"),
    ("/* 主要内容区 */", "/* Main Content */"),
    ("/* Hero 区域 */", "/* Hero Section */"),
    ("/* 调整logo大小 */", "/* Logo size */"),
    ("/* Dashboard 双栏布局 */", "/* Dashboard Two-Column Layout */"),
])

print("Done!")
