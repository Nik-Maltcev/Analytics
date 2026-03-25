with open("frontend/src/components/Step2EnvSetup.vue", 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'highlight-tip' in line and '模式' in line:
        lines[i] = '                      <p class="highlight-tip" @click="useCustomRounds = true">При первом запуске рекомендуем переключиться в режим \'Настроить\' и уменьшить количество раундов для быстрого предпросмотра ➝</p>\n'
        print(f"Fixed line {i+1}")
        break

with open("frontend/src/components/Step2EnvSetup.vue", 'w', encoding='utf-8') as f:
    f.writelines(lines)
