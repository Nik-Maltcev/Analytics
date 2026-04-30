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

    <main class="flex-grow pt-24 pb-12 px-6 max-w-[1024px] mx-auto w-full flex flex-col gap-8">

      <!-- Step 1: Brief -->
      <div class="bg-[#efedef] rounded-xl p-8 border border-[#c5c6cd]">
        <h1 class="text-[30px] leading-[38px] font-semibold tracking-tight text-[#1b1b1d] mb-2">Запуск нового исследования</h1>
        <p class="text-base text-[#44474d] mb-6">Опишите вашу бизнес-идею и выберите категории для анализа.</p>

        <label class="text-sm font-bold text-[#1b1b1d] block mb-2">Опишите вашу бизнес-идею или фокус исследования</label>
        <textarea
          v-model="brief"
          class="w-full bg-[#fbf9fb] border border-[#c5c6cd] rounded-lg py-4 px-4 text-base text-[#1b1b1d] focus:outline-none focus:ring-2 focus:ring-[#3182CE] focus:border-transparent transition-shadow resize-none placeholder:text-[#75777e] mb-4"
          placeholder="например, Оценка потенциала B2B SaaS платформы для логистических компаний в РФ..."
          rows="4"
        ></textarea>

        <!-- Search -->
        <label class="text-sm font-bold text-[#1b1b1d] block mb-2">Категории индустрии</label>
        <div class="relative mb-4">
          <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-[#44474d]">search</span>
          <input
            v-model="searchQuery"
            type="text"
            class="w-full bg-[#fbf9fb] border border-[#c5c6cd] rounded-lg py-3 pl-12 pr-4 text-base text-[#1b1b1d] focus:outline-none focus:ring-2 focus:ring-[#3182CE] focus:border-transparent transition-shadow placeholder:text-[#75777e]"
            placeholder="Поиск категорий..."
            @focus="showAllCategories = true"
          />
        </div>

        <!-- Recommended tags -->
        <div class="flex flex-wrap items-center gap-2 mb-4">
          <span class="text-xs font-medium text-[#44474d] uppercase tracking-wider flex items-center gap-1">
            <span class="material-symbols-outlined text-[16px]">psychology</span> Рекомендуем:
          </span>
          <button
            v-for="tag in recommendedTags"
            :key="tag"
            type="button"
            class="bg-[#fbf9fb] rounded-full px-4 py-1.5 text-xs font-medium border transition-colors"
            :class="isTagSelected(tag) ? 'bg-[#3182CE] text-white border-[#3182CE]' : 'text-[#1b1b1d] border-[#c5c6cd] hover:border-[#3182CE] hover:text-[#3182CE]'"
            @click="toggleByName(tag)"
          >{{ tag }}</button>
        </div>

        <!-- Selected chips -->
        <div v-if="selectedTopics.length > 0" class="flex flex-wrap gap-2 mb-4">
          <span
            v-for="topic in selectedTopics"
            :key="topic.id"
            class="inline-flex items-center gap-1 bg-[#3182CE] text-white text-xs font-medium px-3 py-1.5 rounded-full"
          >
            {{ topic.name }}
            <button type="button" class="ml-1 hover:opacity-70" @click="deselectTopic(topic.id)">×</button>
          </span>
          <span class="text-xs text-[#75777e] self-center">{{ selectedTopics.length }}/5</span>
        </div>
      </div>

      <!-- Category cards grid -->
      <div v-if="!showAllCategories" class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <!-- Large cards -->
        <button
          v-for="cat in featuredLarge"
          :key="cat.name"
          type="button"
          class="col-span-2 bg-[#fbf9fb] border rounded-xl p-6 flex flex-col items-start justify-between h-40 hover:border-[#3182CE] hover:bg-[#f5f3f5] transition-colors group text-left"
          :class="isNameSelected(cat.name) ? 'border-[#3182CE] bg-blue-50' : 'border-[#c5c6cd]'"
          @click="toggleByName(cat.name)"
        >
          <div :class="[cat.bg, cat.text, 'p-3 rounded-lg w-fit']">
            <span class="material-symbols-outlined text-[28px]">{{ cat.icon }}</span>
          </div>
          <div>
            <h3 class="text-xl font-semibold text-[#1b1b1d]">{{ cat.name }}</h3>
            <p class="text-sm text-[#44474d] mt-1">{{ cat.desc }}</p>
          </div>
        </button>

        <!-- Small cards -->
        <button
          v-for="cat in featuredSmall"
          :key="cat.name"
          type="button"
          class="bg-[#fbf9fb] border rounded-xl p-6 flex flex-col items-center justify-center gap-4 h-32 hover:border-[#3182CE] hover:bg-[#f5f3f5] transition-colors group"
          :class="isNameSelected(cat.name) ? 'border-[#3182CE] bg-blue-50' : 'border-[#c5c6cd]'"
          @click="toggleByName(cat.name)"
        >
          <span class="material-symbols-outlined text-[32px] text-[#44474d] group-hover:text-[#3182CE] transition-colors">{{ cat.icon }}</span>
          <span class="text-xs font-medium text-[#1b1b1d] text-center">{{ cat.name }}</span>
        </button>

        <!-- All categories -->
        <button
          type="button"
          class="bg-[#f5f3f5] border border-[#c5c6cd] rounded-xl p-6 flex flex-col items-center justify-center gap-4 h-32 hover:border-[#3182CE] transition-colors group"
          @click="showAllCategories = true"
        >
          <span class="material-symbols-outlined text-[32px] text-[#44474d] group-hover:text-[#3182CE] transition-colors">apps</span>
          <span class="text-xs font-medium text-[#1b1b1d] text-center">Все категории</span>
        </button>
      </div>

      <!-- Full list -->
      <div v-if="showAllCategories">
        <ul class="max-h-72 overflow-y-auto bg-[#fbf9fb] border border-[#c5c6cd] rounded-xl divide-y divide-[#e4e2e4]">
          <li
            v-for="topic in filteredTopics"
            :key="topic.id"
            class="px-5 py-3 cursor-pointer text-sm flex items-center justify-between hover:bg-[#f5f3f5] transition-colors"
            :class="{ 'bg-blue-50 text-[#3182CE] font-medium': isSelected(topic.id) }"
            @click="toggleTopic(topic)"
          >
            <span>{{ topic.name }}</span>
            <span v-if="isSelected(topic.id)" class="material-symbols-outlined text-[18px] text-[#3182CE]">check</span>
          </li>
          <li v-if="filteredTopics.length === 0" class="px-5 py-8 text-center text-sm text-[#75777e]">Категории не найдены</li>
        </ul>
        <button type="button" class="mt-3 text-sm text-[#75777e] hover:text-[#3182CE] transition-colors" @click="showAllCategories = false">← Назад к основным</button>
      </div>

      <!-- Period -->
      <div class="flex items-center gap-4">
        <span class="text-sm font-bold text-[#1b1b1d]">Период:</span>
        <button
          type="button"
          class="px-5 py-2 border rounded-lg text-sm font-medium transition-all"
          :class="days === 14 ? 'bg-black text-white border-black' : 'bg-[#fbf9fb] text-[#1b1b1d] border-[#c5c6cd] hover:border-black'"
          @click="days = 14"
        >14 дней</button>
        <button
          type="button"
          class="px-5 py-2 border rounded-lg text-sm font-medium transition-all flex items-center gap-2"
          :class="days === 30 ? 'bg-black text-white border-black' : 'bg-[#fbf9fb] text-[#1b1b1d] border-[#c5c6cd] hover:border-black'"
          @click="days = 30"
        >
          30 дней
          <span class="text-[10px] font-semibold uppercase tracking-wider px-1.5 py-0.5 rounded"
            :class="days === 30 ? 'bg-white/20 text-white' : 'bg-blue-100 text-blue-700'"
          >рек.</span>
        </button>
      </div>

      <!-- Error -->
      <div v-if="error" class="bg-red-50 text-red-700 border border-red-200 rounded-xl px-4 py-3 text-sm">{{ error }}</div>

      <!-- Action -->
      <div class="flex justify-end">
        <button
          type="button"
          class="flex items-center justify-center gap-2 bg-[#3182CE] text-white px-8 py-4 rounded-xl text-base font-medium hover:bg-blue-700 transition-colors shadow-sm disabled:opacity-40 disabled:cursor-not-allowed"
          :disabled="!canSubmit || loading"
          @click="onSubmit"
        >
          <template v-if="loading">
            <div class="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
            Запускаем…
          </template>
          <template v-else>
            <span class="material-symbols-outlined icon-fill text-[20px]">auto_awesome</span>
            Запустить ИИ-генерацию
          </template>
        </button>
      </div>
    </main>

    <!-- Footer -->
    <footer class="w-full py-12 px-8 flex flex-col md:flex-row justify-between items-center gap-4 bg-slate-50 border-t border-slate-200">
      <span class="text-lg font-black text-slate-900">InsightArch</span>
      <div class="flex flex-wrap justify-center gap-4">
        <a class="text-xs text-slate-500 hover:text-blue-600 transition-colors" href="#">Условия</a>
        <a class="text-xs text-slate-500 hover:text-blue-600 transition-colors" href="#">Конфиденциальность</a>
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
const allTopics = ref([])
const selectedTopicIds = ref([])
const searchQuery = ref('')
const days = ref(14)
const loading = ref(false)
const error = ref('')
const showAllCategories = ref(false)

const recommendedTags = ['Маркетинг', 'AI', 'Разработка', 'Еда', 'Инвестиции']

const featuredLarge = [
  { icon: 'shopping_cart', name: 'Маркетплейсы', desc: 'Торговые площадки, e-commerce', bg: 'bg-[#d6e3ff]', text: 'text-[#0d1c32]' },
  { icon: 'code', name: 'Разработка', desc: 'ПО, SaaS, облачные сервисы', bg: 'bg-[#d6e3ff]', text: 'text-[#0d1c32]' },
]

const featuredSmall = [
  { icon: 'campaign', name: 'Маркетинг' },
  { icon: 'restaurant', name: 'Еда' },
  { icon: 'health_and_safety', name: 'Здоровье' },
  { icon: 'savings', name: 'Инвестиции' },
  { icon: 'travel_explore', name: 'Путешествия' },
]

const selectedTopics = computed(() => {
  return allTopics.value.filter(t => selectedTopicIds.value.includes(t.id))
})

const filteredTopics = computed(() => {
  if (!searchQuery.value) return allTopics.value
  const q = searchQuery.value.toLowerCase()
  return allTopics.value.filter(t => t.name.toLowerCase().includes(q))
})

const canSubmit = computed(() => {
  return brief.value.trim() !== '' && selectedTopicIds.value.length > 0 && selectedTopicIds.value.length <= 5
})

function isSelected(id) {
  return selectedTopicIds.value.includes(id)
}

function isNameSelected(name) {
  const topic = allTopics.value.find(t => t.name.toLowerCase() === name.toLowerCase())
  return topic ? isSelected(topic.id) : false
}

function isTagSelected(tag) {
  return isNameSelected(tag)
}

function toggleTopic(topic) {
  const idx = selectedTopicIds.value.indexOf(topic.id)
  if (idx >= 0) {
    selectedTopicIds.value.splice(idx, 1)
  } else if (selectedTopicIds.value.length < 5) {
    selectedTopicIds.value.push(topic.id)
  }
}

function toggleByName(name) {
  const topic = allTopics.value.find(t => t.name.toLowerCase() === name.toLowerCase())
  if (topic) toggleTopic(topic)
}

function deselectTopic(id) {
  const idx = selectedTopicIds.value.indexOf(id)
  if (idx >= 0) selectedTopicIds.value.splice(idx, 1)
}

async function loadTopics() {
  try {
    const response = await getExternalTopics()
    if (response.success) {
      allTopics.value = response.data.topics || []
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
