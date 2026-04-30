<template>
  <div class="bg-[#fbf9fb] text-[#1b1b1d] min-h-screen flex flex-col font-['Inter'] antialiased pt-16">
    <!-- Navbar -->
    <nav class="fixed top-0 left-0 w-full z-50 flex items-center justify-between px-8 h-16 max-w-7xl mx-auto bg-white border-b border-slate-200 shadow-sm right-0">
      <div class="text-xl font-bold text-slate-900 tracking-tight">InsightArch</div>
      <ul class="hidden md:flex space-x-8 items-center h-full">
        <li><a class="text-sm font-medium text-slate-600 hover:text-blue-700 transition-colors cursor-pointer">Дашборд</a></li>
        <li><a class="text-sm font-medium text-slate-600 hover:text-blue-700 transition-colors cursor-pointer">Рыночные отчеты</a></li>
        <li><a class="text-sm font-medium text-slate-600 hover:text-blue-700 transition-colors cursor-pointer">Методология</a></li>
        <li><a class="text-sm font-medium text-slate-600 hover:text-blue-700 transition-colors cursor-pointer">Цены</a></li>
      </ul>
      <div class="flex items-center space-x-4">
        <button class="text-sm font-medium px-4 py-2 bg-slate-900 text-white rounded-lg hover:opacity-80 transition-opacity" @click="goToResearch">Начать</button>
      </div>
    </nav>

    <!-- Hero -->
    <section class="max-w-7xl mx-auto px-8 py-16 mt-8">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
        <div class="flex flex-col gap-8">
          <div class="inline-flex items-center gap-2 px-3 py-1 bg-[#efedef] rounded-full border border-[#c5c6cd] w-fit">
            <span class="material-symbols-outlined text-[16px] text-black icon-fill">bolt</span>
            <span class="text-xs font-semibold text-[#44474d] uppercase tracking-wider">АНАЛИТИЧЕСКИЙ ДВИЖОК НОВОГО ПОКОЛЕНИЯ</span>
          </div>
          <h1 class="text-4xl font-bold tracking-tight leading-tight text-[#1b1b1d]">AI-аналитика рынка за часы, а не недели.</h1>
          <p class="text-lg text-[#44474d] max-w-xl leading-relaxed">
            Забудьте о медленных агентствах. Наш ИИ синтезирует данные из тысяч актуальных глобальных и локальных источников в режиме реального времени, предоставляя глубокие отчеты институционального уровня.
          </p>
          <div class="flex flex-wrap items-center gap-4 pt-2">
            <button class="bg-black text-white text-base font-medium px-6 py-3 rounded-lg flex items-center gap-2 hover:opacity-90 transition-opacity" @click="goToResearch">
              Начать исследование
              <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
            </button>
            <button class="bg-transparent text-black border border-[#75777e] text-base font-medium px-6 py-3 rounded-lg flex items-center gap-2 hover:bg-[#efedef] transition-colors">
              Пример отчета
            </button>
          </div>
        </div>
        <div class="relative h-[500px] w-full rounded-xl overflow-hidden border border-[#c5c6cd] bg-white shadow-[0px_4px_24px_rgba(10,25,47,0.06)]">
          <div class="absolute inset-0 bg-gradient-to-br from-[#f5f3f5] to-white"></div>
          <img
            alt="Data Dashboard Visualization"
            class="w-full h-full object-cover mix-blend-multiply opacity-90"
            src="https://lh3.googleusercontent.com/aida-public/AB6AXuDs-ZhhF5jjcfmib88iFsjTGOyuNGN772kSnvZbyuMgqNNVhcFO8nZdYjfRDyWkwMXP9lsAbVQMOQ5vVQlJICOJFVwMmY-edw7Gp2InnipoCJbBgt92T1ZeaVwwm06syeXwH54bzRGF5TJCLxJ8sMu_REbTTkK77fi7vMAFSlTLmzF40849wcD93Fgo7VKaScHC4Dv_XT0sD4b186VMaay4R0-sVsKJ9Pj1te54daygfiVyTIlsaN09LUOtqQzM5sjAI_ziqipg71Y"
          />
        </div>
      </div>
    </section>

    <!-- Value Props -->
    <section class="bg-[#f5f3f5] py-16 border-y border-[#c5c6cd]">
      <div class="max-w-7xl mx-auto px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl font-semibold tracking-tight text-[#1b1b1d] mb-2">Институциональная строгость, ускоренная</h2>
          <p class="text-base text-[#44474d] max-w-2xl mx-auto">Наш проприетарный ИИ-конвейер преобразует фрагментированные глобальные данные в согласованные и проверенные потоки информации.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="bg-white border border-[#c5c6cd] rounded-xl p-8 flex flex-col gap-4 shadow-[0px_2px_8px_rgba(10,25,47,0.02)] hover:shadow-[0px_8px_24px_rgba(10,25,47,0.06)] transition-shadow">
            <div class="w-12 h-12 bg-[#0d1c32] rounded-lg flex items-center justify-center text-[#76849f]">
              <span class="material-symbols-outlined icon-fill">sensors</span>
            </div>
            <h3 class="text-2xl font-semibold text-[#1b1b1d]">Сбор данных в реальном времени</h3>
            <p class="text-base text-[#44474d] flex-grow">Анализирует только свежие, динамически обновляемые источники из лучших мировых репозиториев.</p>
          </div>
          <div class="bg-white border border-[#c5c6cd] rounded-xl p-8 flex flex-col gap-4 shadow-[0px_2px_8px_rgba(10,25,47,0.02)] hover:shadow-[0px_8px_24px_rgba(10,25,47,0.06)] transition-shadow">
            <div class="w-12 h-12 bg-[#0d1c32] rounded-lg flex items-center justify-center text-[#76849f]">
              <span class="material-symbols-outlined icon-fill">memory</span>
            </div>
            <h3 class="text-2xl font-semibold text-[#1b1b1d]">Продвинутая ИИ-обработка</h3>
            <p class="text-base text-[#44474d] flex-grow">Собственные модели перекрестно проверяют данные для обеспечения абсолютной точности.</p>
          </div>
          <div class="bg-white border border-[#c5c6cd] rounded-xl p-8 flex flex-col gap-4 shadow-[0px_2px_8px_rgba(10,25,47,0.02)] hover:shadow-[0px_8px_24px_rgba(10,25,47,0.06)] transition-shadow">
            <div class="w-12 h-12 bg-[#0d1c32] rounded-lg flex items-center justify-center text-[#76849f]">
              <span class="material-symbols-outlined icon-fill">lab_profile</span>
            </div>
            <h3 class="text-2xl font-semibold text-[#1b1b1d]">Профессиональный результат</h3>
            <p class="text-base text-[#44474d] flex-grow">Генерирует готовые для руководства отчеты с подробными ссылками и матрицами данных.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Comparison -->
    <section class="max-w-7xl mx-auto px-8 py-16">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-semibold tracking-tight text-[#1b1b1d] mb-2">ROI современной аналитики</h2>
        <p class="text-base text-[#44474d] max-w-2xl mx-auto">Сравните старую парадигму маркетинговых исследований с точностью и скоростью InsightArch.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
        <!-- Traditional -->
        <div class="bg-[#fbf9fb] border border-[#c5c6cd] rounded-xl p-8 flex flex-col gap-4 opacity-70">
          <div class="flex items-center justify-between border-b border-[#c5c6cd] pb-2">
            <h3 class="text-2xl font-semibold text-[#44474d]">Обычное агентство</h3>
            <span class="material-symbols-outlined text-[#75777e]">hourglass_empty</span>
          </div>
          <ul class="flex flex-col gap-4 mt-2">
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-red-600 mt-1 text-[20px]">close</span>
              <div><span class="text-sm font-medium text-[#44474d] block">СТОИМОСТЬ</span><span class="text-base font-semibold">50 000 ₽</span></div>
            </li>
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-red-600 mt-1 text-[20px]">close</span>
              <div><span class="text-sm font-medium text-[#44474d] block">СРОКИ</span><span class="text-base font-semibold">2-3 недели</span></div>
            </li>
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-red-600 mt-1 text-[20px]">close</span>
              <div><span class="text-sm font-medium text-[#44474d] block">АКТУАЛЬНОСТЬ</span><span class="text-base font-semibold">Устаревшие данные</span></div>
            </li>
          </ul>
        </div>
        <!-- InsightArch -->
        <div class="bg-white border border-black rounded-xl p-8 flex flex-col gap-4 relative shadow-[0px_8px_32px_rgba(10,25,47,0.08)]">
          <div class="absolute -top-3 right-8 bg-black text-white text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wider">Рекомендуется</div>
          <div class="flex items-center justify-between border-b border-[#c5c6cd] pb-2">
            <h3 class="text-2xl font-semibold text-[#1b1b1d]">Сервис InsightArch</h3>
            <span class="material-symbols-outlined text-black icon-fill">speed</span>
          </div>
          <ul class="flex flex-col gap-4 mt-2">
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-black mt-1 text-[20px]">check</span>
              <div><span class="text-sm font-medium text-[#44474d] block">СТОИМОСТЬ</span><span class="text-base font-semibold">10 000 ₽</span></div>
            </li>
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-black mt-1 text-[20px]">check</span>
              <div><span class="text-sm font-medium text-[#44474d] block">СРОКИ</span><span class="text-base font-semibold">2 часа</span></div>
            </li>
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-black mt-1 text-[20px]">check</span>
              <div><span class="text-sm font-medium text-[#44474d] block">АКТУАЛЬНОСТЬ</span><span class="text-base font-semibold">ИИ-синтез в реальном времени</span></div>
            </li>
          </ul>
          <div class="mt-auto pt-8">
            <button class="w-full bg-black text-white text-base font-medium px-6 py-3 rounded-lg hover:opacity-90 transition-opacity" @click="goToResearch">Начать исследование</button>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="w-full py-12 px-8 flex flex-col md:flex-row justify-between items-center gap-4 bg-slate-50 border-t border-slate-200">
      <div class="text-lg font-black text-slate-900">InsightArch</div>
      <p class="text-xs text-slate-500">© 2025 InsightArch Analytics. Точность в рыночной разведке.</p>
      <ul class="flex flex-wrap gap-4 items-center justify-center">
        <li><a class="text-xs text-slate-500 hover:text-blue-600 transition-colors" href="#">Условия использования</a></li>
        <li><a class="text-xs text-slate-500 hover:text-blue-600 transition-colors" href="#">Политика конфиденциальности</a></li>
        <li><a class="text-xs text-slate-500 hover:text-blue-600 transition-colors" href="#">Методология</a></li>
        <li><a class="text-xs text-slate-500 hover:text-blue-600 transition-colors" href="#">Поддержка</a></li>
      </ul>
    </footer>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function goToResearch() {
  router.push({ name: 'Research' })
}
</script>
