import re

with open('frontend/src/views/Home.vue', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the hero description paragraph
old = '即使只有一段文字，<span class="highlight-bold">MiroFish</span> 也能基于其中的现实种子，全自动生成与之对应的至多<span class="highlight-orange">百万级Agent</span>构成的平行世界。通过上帝视角注入变量，在复杂的群体交互中寻找动态环境下的<span class="highlight-code">\u201c局部最优解\u201d</span>'
new = 'Даже из одного абзаца текста <span class="highlight-bold">MiroFish</span> извлечёт реальные зёрна и автоматически создаст параллельный мир из до <span class="highlight-orange">миллиона агентов</span>. Внедряйте переменные с позиции наблюдателя и находите <span class="highlight-code">\u00abлокальный оптимум\u00bb</span> в сложных групповых взаимодействиях'

if old in content:
    content = content.replace(old, new)
    print('Replaced hero desc')
else:
    print('Hero desc NOT FOUND')

with open('frontend/src/views/Home.vue', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
