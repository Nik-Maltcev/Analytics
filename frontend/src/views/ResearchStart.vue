<template>
  <div class="bg-[#fbf9fb] text-[#1b1b1d] min-h-screen flex flex-col font-['Inter'] antialiased pt-16">
    <!-- Navbar -->
    <nav class="fixed top-0 left-0 w-full z-50 flex items-center justify-between px-8 h-16 max-w-7xl mx-auto bg-white border-b border-slate-200 shadow-sm right-0">
      <div class="flex items-center gap-8">
        <span class="text-xl font-bold text-slate-900 tracking-tight cursor-pointer" @click="$router.push('/')">InsightArch</span>
        <div class="hidden md:flex items-center gap-4">
          <a class="text-sm font-medium text-blue-600 border-b-2 border-blue-600 pb-1">Дашборд</a>
          <a class="text-sm font-medium text-slate-600 hover:text-blue-700 transition-colors cursor-pointer">Отчеты</a>
          <a class="text-sm font-medium text-slate-600 hover:text-blue-700 transition-colors cursor-pointer">Методология</a>
          <a class="text-sm font-medium text-slate-600 hover:text-blue-700 transition-colors cursor-pointer">Цены</a>
        </div>
      </div>
    </nav>

    <!-- Main -->
    <main class="flex-grow pt-24 pb-16 px-8 max-w-7xl mx-auto w-full flex flex-col items-center justify-center">
      <div class="w-full max-w-2xl bg-white border border-[#E2E8F0] rounded-lg p-8 shadow-[0px_4px_12px_rgba(10,25,47,0.05)]">
        <div class="mb-8 text-center">
          <h1 class="text-3xl font-semibold tracking-tight text-[#1b1b1d] mb-2">Запуск нового исследования</h1>
          <p class="text-base text-[#44474d]">Опишите вашу бизнес-идею или фокус исследования для генерации подробного отчета.</p>
        </div>

        <form class="space-y-4" @submit.prevent="onSubmit">
          <!-- Text Area -->
          <div class="flex flex-col gap-1">
            <label class="text-sm font-bold text-[#1b1b1d]" for="research-focus">Опишите вашу бизнес-идею или фокус исследования</label>
            <textarea
              id="research-focus"
              v-model="brief"
              class="w-full border border-[#E2E8F0] rounded p-3 bg-white text-[#1b1b1d] text-base focus:border-[#3182CE] focus:ring-1 focus:ring-[#3182CE] outline-none transition-colors resize-none placeholder:text-[#75777e]"
              placeholder="например, Оценка потенциала B2B SaaS платформы для логистических компаний в РФ..."
              rows="5"
            ></textarea>
          </div>

          <!-- Category dropdown -->
          <div class="flex flex-col gap-1">
            <label class="text-sm font-bold text-[#1b1b1d]" for="category">Категория индустрии</label>
            <div class="relative">
              <select
                id="category"
                v-model="selectedTopicIds"
                multiple
                class="w-full border border-[#E2E8F0] rounded p-3 pr-10 bg-white text-[#1b1b1d] text-base focus:border-[#3182CE] focus:ring-1 focus:ring-[#3182CE] outline-none transition-colors"
                :size="Math.min(topics.length, 8)"
              >
                <option v-for="topic in topics" :key="topic.id" :value="topic.id">
                  {{ topic.name }}
                </option>
              </select>
            </div>
            <p class="text-xs text-[#75777e] mt-1">Выберите одну или несколько категорий (до 5). Зажмите Ctrl для мультиселекта.</p>
          </div>

          <!-- Period -->
          <div class="flex flex-col gap-1">
            <label class="text-sm font-bold text-[#1b1b1d]">Период анализа</label>
            <div class="flex gap-3">
              <button
                type="button"
                class="px-5 py-2.5 border rounded-lg text-sm font-medium transition-all"
                :class="days === 7 ? 'bg-black text-white border-black' : 'bg-white text-[#1b1b1d] border-[#E2E8F0] hover:border-black'"
                @click="days = 7"
              >7 дней</button>
              <button
                type="button"
                class="px-5 py-2.5 border rounded-lg text-sm font-medium transition-all"
                :class="days === 14 ? 'bg-black text-white border-black' : 'bg-white text-[#1b1b1d] border-[#E2E8F0] hover:border-black'"
                @click="days = 14"
              >14 дней</button>
              <button
                type="button"
                class="px-5 py-2.5 border rounded-lg text-sm font-medium transition-all"
                :class="days === 30 ? 'bg-black text-white border-black' : 'bg-white text-[#1b1b1d] border-[#E2E8F0] hover:border-black'"
                @click="days = 30"
              >30 дней</button>
            </div>
          </div>

          <!-- Error -->
          <div v-if="error" class="bg-red-50 text-red-700 border border-red-200 rounded-lg px-4 py-3 text-sm">{{ error }}</div>

          <!-- Actions -->
          <div class="pt-4 flex flex-col items-center gap-4 mt-4 border-t border-[#E2E8F0]">
            <button
              type="submit"
              class="w-full flex items-center justify-center gap-2 bg-[#3182CE] text-white px-4 py-3 rounded text-base font-medium hover:bg-blue-700 transition-colors shadow-sm disabled:opacity-40 disabled:cursor-not-allowed"
              :disabled="!canSubmit || loading"
            >
              <template v-if="loading">
                <div class="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
                Запускаем…
              </template>
              <template v-else>
                <span class="material-symbols-outlined icon-fill">auto_awesome</span>
                Запустить ИИ-генерацию
              </template>
            </button>
            <div class="flex items-start gap-1 text-[#44474d] max-w-md mx-auto">
              <span class="material-symbols-outlined text-[18px] mt-[2px] text-[#b9c7e4]">info</span>
              <p class="text-sm text-center">Наш ИИ просканирует тысячи актуальных источников, чтобы предоставить самую свежую аналитику рынка.</p>
            </div>
          </div>
        </form>
      </div>
    </main>

    <!-- Footer -->
    <footer class="w-full py-12 px-8 flex flex-col md:flex-row justify-between items-center gap-4 bg-slate-50 border-t border-slate-200">
      <span class="text-lg font-black text-slate-900">InsightArch</span>
      <div class="flex flex-wrap justify-center gap-4">
        <a class="text-xs text-slate-500 hover:text-blue-600 transition-colors" href="#">Условия использования</a>
        <a class="text-xs text-slate-500 hover:text-blue-600 transition-colors" href="#">Политика конфиденциальности</a>
        <a class="text-xs text-slate-500 hover:text-blue-600 transition-colors" href="#">Методология</a>
        <a class="text-xs text-slate-500 hover:text-blue-600 transition-colors" href="#">Поддержка</a>
      </div>
      <p class="text-xs text-slate-500">© 2025 InsightArch Analytics.</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { generateMarketResearch, getExternalTopics } from '../api/graph'
import { loadTailwind, unloadTailwind } from '../utils/tailwind-loader'

const router = useRouter()

const brief = ref('')
const topics = ref([])
const selectedTopicIds = ref([])
const days = ref(30)
const loading = ref(false)
const error = ref('')

const canSubmit = computed(() => {
  return brief.value.trim() !== '' && selectedTopicIds.value.length > 0 && selectedTopicIds.value.length <= 5
})

async function loadTopics() {
  try {
    const response = await getExternalTopics()
    if (response.success) {
      topics.value = response.data.topics || []
    }
  } catch (err) {
    console.error('Failed to load topics:', err)
  }
}

async function onSubmit() {
  if (!canSubmit.value) return
  loading.value = true
  error.value = ''
  try {
    const response = await generateMarketResearch({
      topic_ids: selectedTopicIds.value,
      brief: brief.value,
      days: days.value,
      project_name: `Research: ${brief.value.slice(0, 50)}`,
    })
    if (response.success && response.data?.project_id) {
      router.push({ name: 'Process', params: { projectId: response.data.project_id } })
    } else {
      error.value = response.error || 'Не удалось запустить исследование'
    }
  } catch (err) {
    error.value = err?.response?.data?.error || err?.message || 'Ошибка при запуске исследования'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadTailwind()
  loadTopics()
})

onUnmounted(() => unloadTailwind())
</script>
