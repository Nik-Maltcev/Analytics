"""
Translate remaining Chinese text in frontend components to Russian.
"""
import re

replacements = {
    # Step2EnvSetup.vue
    "frontend/src/components/Step2EnvSetup.vue": [
        (
            "若首次运行，强烈建议切换至'Настроить模式'减少模拟р数，以便快速预览效果并降低报错风险 ➝",
            "При первом запуске рекомендуем переключиться в 'Настроить' и уменьшить количество раундов для быстрого предпросмотра ➝"
        ),
        ("<!-- 模拟р数配置 - 只有在配置生成完成且р数计算出来后才显示 -->", "<!-- Настройка раундов - показывать только после генерации конфигурации -->"),
        ("<!-- 基本信息 -->", "<!-- Основная информация -->"),
        ("<!-- 简介 -->", "<!-- Описание -->"),
        ("<!-- 关注话题 -->", "<!-- Темы интереса -->"),
        ("<!-- 详细人设 -->", "<!-- Подробная предыстория -->"),
        ("<!-- 人设维度概览 -->", "<!-- Обзор характеристик -->"),
    ],
}

# Also search for any remaining Chinese in all Step components
import glob

step_files = glob.glob("frontend/src/components/Step*.vue")
step_files += glob.glob("frontend/src/views/*.vue")
step_files += glob.glob("frontend/src/components/*.vue")

# Common Chinese patterns to translate (comments and visible text)
common_replacements = [
    # Comments
    ("<!-- 边详情 -->", "<!-- Edge details -->"),
    ("<!-- 自环组详情 -->", "<!-- Self-loop group details -->"),
    ("<!-- 普通边详情 -->", "<!-- Regular edge details -->"),
    ("<!-- 加载状态 -->", "<!-- Loading state -->"),
    ("<!-- 等待/空状态 -->", "<!-- Waiting/empty state -->"),
    ("<!-- 底部图例 (Bottom Left) -->", "<!-- Bottom legend -->"),
    ("<!-- 显示边标签开关 -->", "<!-- Edge labels toggle -->"),
]

# JS comment replacements
js_comment_replacements = [
    ("// 默认显示边标签", "// Show edge labels by default"),
    ("// 展开的自环项", "// Expanded self-loop items"),
    ("// 模拟结束后的提示", "// Post-simulation hint"),
]

def process_file(filepath, specific_replacements=None):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  Error reading {filepath}: {e}")
        return False

    original = content
    
    # Apply specific replacements
    if specific_replacements:
        for old, new in specific_replacements:
            if old in content:
                content = content.replace(old, new)
                print(f"  Replaced: {old[:60]}...")
    
    # Apply common replacements
    for old, new in common_replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"  Replaced comment: {old[:60]}...")
    
    for old, new in js_comment_replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"  Replaced JS comment: {old[:60]}...")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    changed_files = []
    
    # Process files with specific replacements
    for filepath, repls in replacements.items():
        print(f"\nProcessing: {filepath}")
        if process_file(filepath, repls):
            changed_files.append(filepath)
    
    # Process all component files for common replacements
    all_files = set(step_files)
    for filepath in sorted(all_files):
        if filepath.replace("\\", "/") not in replacements:
            print(f"\nProcessing: {filepath}")
            if process_file(filepath):
                changed_files.append(filepath)
    
    # Now find any remaining Chinese characters in frontend
    print("\n\n=== Remaining Chinese text in frontend ===")
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')
    
    all_vue_files = glob.glob("frontend/src/**/*.vue", recursive=True)
    all_vue_files += glob.glob("frontend/src/**/*.js", recursive=True)
    
    for filepath in sorted(set(all_vue_files)):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            for i, line in enumerate(lines, 1):
                matches = chinese_pattern.findall(line)
                if matches:
                    stripped = line.strip()
                    # Skip pure comments
                    is_comment = stripped.startswith('//') or stripped.startswith('/*') or stripped.startswith('*') or stripped.startswith('<!--')
                    marker = "  [COMMENT]" if is_comment else "  [TEXT]"
                    print(f"  {filepath}:{i}{marker} {''.join(matches)}")
        except Exception:
            pass
    
    print(f"\n\nChanged {len(changed_files)} files: {changed_files}")


if __name__ == "__main__":
    main()
