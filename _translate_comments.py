# -*- coding: utf-8 -*-
"""Translate remaining HTML comments in Home.vue and any other files."""

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
    ("<!-- 顶部导航栏 -->", "<!-- Top Navbar -->"),
    ("<!-- 上半部分：Hero 区域 -->", "<!-- Hero Section -->"),
    ("<!-- Logo 区域 -->", "<!-- Logo Area -->"),
    ("<!-- 下半部分：双栏布局 -->", "<!-- Two-Column Layout -->"),
    ("<!-- 左栏：状态与步骤 -->", "<!-- Left: Status & Steps -->"),
    ("<!-- 数据指标卡片 -->", "<!-- Metrics Cards -->"),
    ("<!-- 项目模拟步骤介绍 (新增区域) -->", "<!-- Simulation Steps -->"),
    ("<!-- 右栏：交互控制台 -->", "<!-- Right: Console -->"),
])

print("Comments cleanup done!")
