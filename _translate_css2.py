# -*- coding: utf-8 -*-
"""Translate remaining CSS comments in Home.vue."""

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
    ("/* 左侧面板 */", "/* Left Panel */"),
    ("/* 项目模拟步骤介绍 */", "/* Simulation Steps */"),
    ("/* 右侧交互控制台 */", "/* Right Console */"),
    ("/* 外部实线 */", "/* outer border */"),
    ("/* 内边距形成双重边框感 */", "/* padding for double border effect */"),
    ("/* 可点击状态（非禁用） */", "/* Clickable state (not disabled) */"),
    ("/* 引导动画：微妙的边框脉冲 */", "/* Guide animation: subtle border pulse */"),
])

# Also check all other Vue files for remaining Chinese in CSS/comments
import glob, re
pattern = re.compile(r'[\u4e00-\u9fff]')
for f in glob.glob('frontend/src/**/*.vue', recursive=True):
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        if pattern.search(line):
            print(f"  REMAINING: {f}:{i}: {line.strip()[:80]}")

print("Done!")
