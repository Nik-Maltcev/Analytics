<template>
  <div class="tw-page bg-[#fbf9fb] text-[#1b1b1d] min-h-screen flex flex-col font-['Inter'] antialiased pt-16">
    <nav class="fixed top-0 left-0 w-full z-50 flex items-center px-8 h-16 max-w-7xl mx-auto bg-white border-b border-slate-200 shadow-sm right-0">
      <router-link to="/" class="text-xl font-bold text-slate-900 tracking-tight">InsightArch</router-link>
    </nav>

    <main class="flex-grow pt-24 pb-16 px-8 max-w-3xl mx-auto w-full">
      <h1 class="text-3xl font-bold mb-8">Политика конфиденциальности</h1>
      <p class="text-sm text-slate-500 mb-8">Дата вступления в силу: 1 мая 2026 г.</p>

      <div class="space-y-6 text-base leading-relaxed text-[#44474d]">
        <section>
          <h2 class="text-xl font-semibold text-[#1b1b1d] mb-3">1. Общие положения</h2>
          <p>Настоящая Политика конфиденциальности определяет порядок обработки и защиты персональных данных пользователей сервиса InsightArch (далее — Сервис).</p>
          <p class="mt-2">Исполнитель: Мальцев Никита Евгеньевич, самозанятый (НПД), ИНН 165924805367.</p>
        </section>

        <section>
          <h2 class="text-xl font-semibold text-[#1b1b1d] mb-3">2. Какие данные мы собираем</h2>
          <ul class="list-disc pl-6 space-y-2">
            <li><strong>Данные исследования</strong> — бриф, выбранные категории, параметры анализа. Используются для выполнения запроса.</li>
            <li><strong>Технические данные</strong> — IP-адрес, тип устройства, данные о сессии.</li>
            <li><strong>Платёжные данные</strong> — обрабатываются исключительно платёжным провайдером. Мы не храним данные банковских карт.</li>
          </ul>
        </section>

        <section>
          <h2 class="text-xl font-semibold text-[#1b1b1d] mb-3">3. Цели обработки</h2>
          <ul class="list-disc pl-6 space-y-1">
            <li>Предоставление услуг Сервиса (генерация аналитических отчётов)</li>
            <li>Обработка платежей</li>
            <li>Улучшение качества Сервиса</li>
          </ul>
        </section>

        <section>
          <h2 class="text-xl font-semibold text-[#1b1b1d] mb-3">4. Хранение и защита</h2>
          <p>Данные хранятся на защищённых серверах. Мы не передаём персональные данные третьим лицам, за исключением случаев, предусмотренных законодательством РФ.</p>
        </section>

        <section>
          <h2 class="text-xl font-semibold text-[#1b1b1d] mb-3">5. Права пользователя</h2>
          <p>Вы имеете право запросить удаление ваших данных, написав на email поддержки.</p>
        </section>

        <section>
          <h2 class="text-xl font-semibold text-[#1b1b1d] mb-3">6. Контакты</h2>
          <p>Email: <strong>support@insightarch.ru</strong></p>
          <p>Мальцев Никита Евгеньевич, ИНН 165924805367</p>
        </section>
      </div>
    </main>
  </div>
</template>

<script setup>
</script>
