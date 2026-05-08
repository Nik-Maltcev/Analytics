<template>
  <div class="tw-page bg-[#fbf9fb] text-[#1b1b1d] min-h-screen flex flex-col font-['Inter'] antialiased pt-16">
    <!-- Navbar -->
    <nav class="fixed top-0 left-0 w-full z-50 flex items-center justify-between px-8 h-16 max-w-7xl mx-auto bg-white border-b border-slate-200 shadow-sm right-0">
      <div class="flex items-center gap-8">
        <span class="text-xl font-bold text-slate-900 tracking-tight cursor-pointer" @click="$router.push('/')">InsightArch</span>
        <div class="hidden md:flex items-center gap-4">
          <a class="text-sm font-medium text-blue-600 border-b-2 border-blue-600 pb-1">Dashboard</a>
          <a class="text-sm font-medium text-slate-600 hover:text-blue-700 transition-colors cursor-pointer">Reports</a>
          <a class="text-sm font-medium text-slate-600 hover:text-blue-700 transition-colors cursor-pointer">Methodology</a>
          <a class="text-sm font-medium text-slate-600 hover:text-blue-700 transition-colors cursor-pointer">Pricing</a>
        </div>
      </div>
    </nav>

    <main class="flex-grow pt-24 pb-12 px-6 max-w-[1024px] mx-auto w-full flex flex-col gap-8">

      <!-- Step 1: Brief -->
      <div class="bg-[#efedef] rounded-xl p-8 border border-[#c5c6cd]">
        <h1 class="text-[30px] leading-[38px] font-semibold tracking-tight text-[#1b1b1d] mb-2">Start New Research</h1>
        <p class="text-base text-[#44474d] mb-6">Describe your business idea or research focus. Our AI will automatically select the most relevant data sources.</p>

        <label class="text-sm font-bold text-[#1b1b1d] block mb-2">Describe your business idea or research focus</label>
        <textarea
          v-model="brief"
          class="w-full bg-[#fbf9fb] border border-[#c5c6cd] rounded-lg py-4 px-4 text-base text-[#1b1b1d] focus:outline-none focus:ring-2 focus:ring-[#3182CE] focus:border-transparent transition-shadow resize-none placeholder:text-[#75777e] mb-4"
          placeholder="e.g., Market research for a food delivery app targeting urban millennials..."
          rows="4"
        ></textarea>

        <!-- AI Source Selection Button -->
        <button
          type="button"
          class="flex items-center gap-2 bg-white border border-[#c5c6cd] rounded-lg px-5 py-3 text-sm font-medium text-[#1b1b1d] hover:border-[#3182CE] hover:text-[#3182CE] transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
          :disabled="!brief.trim() || aiSelecting"
          @click="runAiSelection"
        >
          <template v-if="aiSelecting">
            <div class="w-4 h-4 border-2 border-[#3182CE]/30 border-t-[#3182CE] rounded-full animate-spin"></div>
            AI is selecting sources...
          </template>
          <template v-else>
            <span class="material-symbols-outlined text-[18px]">auto_awesome</span>
            Auto-select sources with AI
          </template>
        </button>
      </div>

      <!-- Step 2: AI-selected sources (shown after AI selection) -->
      <div v-if="selectedSources.length > 0" class="bg-white rounded-xl p-8 border border-[#c5c6cd]">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-xl font-semibold text-[#1b1b1d]">Selected Data Sources</h2>
          <span class="text-xs text-[#75777e]">{{ selectedSources.length }} sources selected</span>
        </div>
        <p class="text-sm text-[#44474d] mb-6">AI picked these sources based on your brief. You can adjust the selection.</p>

        <!-- Source groups -->
        <div class="flex flex-col gap-6">
          <!-- Twitter -->
          <div v-if="twitterSources.length > 0">
            <div class="flex items-center gap-2 mb-3">
              <div class="w-6 h-6 bg-black rounded flex items-center justify-center">
                <span class="text-white text-xs font-bold">𝕏</span>
              </div>
              <span class="text-sm font-semibold text-[#1b1b1d]">Twitter / X</span>
              <span class="text-xs text-[#75777e]">({{ twitterSources.length }})</span>
            </div>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="src in twitterSources"
                :key="src.id"
                class="inline-flex items-center gap-1 bg-gray-100 text-sm px-3 py-1.5 rounded-full border border-gray-200"
              >
                @{{ src.name }}
                <button type="button" class="ml-1 text-gray-400 hover:text-red-500" @click="removeSource(src.id)">×</button>
              </span>
            </div>
          </div>

          <!-- Reddit -->
          <div v-if="redditSources.length > 0">
            <div class="flex items-center gap-2 mb-3">
              <div class="w-6 h-6 bg-orange-500 rounded flex items-center justify-center">
                <span class="text-white text-xs font-bold">R</span>
              </div>
              <span class="text-sm font-semibold text-[#1b1b1d]">Reddit</span>
              <span class="text-xs text-[#75777e]">({{ redditSources.length }})</span>
            </div>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="src in redditSources"
                :key="src.id"
                class="inline-flex items-center gap-1 bg-orange-50 text-sm px-3 py-1.5 rounded-full border border-orange-200"
              >
                r/{{ src.name }}
                <button type="button" class="ml-1 text-gray-400 hover:text-red-500" @click="removeSource(src.id)">×</button>
              </span>
            </div>
          </div>

          <!-- Telegram -->
          <div v-if="telegramSources.length > 0">
            <div class="flex items-center gap-2 mb-3">
              <div class="w-6 h-6 bg-blue-500 rounded flex items-center justify-center">
                <span class="text-white text-xs font-bold">T</span>
              </div>
              <span class="text-sm font-semibold text-[#1b1b1d]">Telegram</span>
              <span class="text-xs text-[#75777e]">({{ telegramSources.length }})</span>
            </div>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="src in telegramSources"
                :key="src.id"
                class="inline-flex items-center gap-1 bg-blue-50 text-sm px-3 py-1.5 rounded-full border border-blue-200"
              >
                {{ src.name }}
                <button type="button" class="ml-1 text-gray-400 hover:text-red-500" @click="removeSource(src.id)">×</button>
              </span>
            </div>
          </div>

          <!-- Forums -->
          <div v-if="forumSources.length > 0">
            <div class="flex items-center gap-2 mb-3">
              <div class="w-6 h-6 bg-emerald-600 rounded flex items-center justify-center">
                <span class="text-white text-xs font-bold">F</span>
              </div>
              <span class="text-sm font-semibold text-[#1b1b1d]">Forums</span>
              <span class="text-xs text-[#75777e]">({{ forumSources.length }})</span>
            </div>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="src in forumSources"
                :key="src.id"
                class="inline-flex items-center gap-1 bg-emerald-50 text-sm px-3 py-1.5 rounded-full border border-emerald-200"
              >
                {{ src.name }}
                <button type="button" class="ml-1 text-gray-400 hover:text-red-500" @click="removeSource(src.id)">×</button>
              </span>
            </div>
          </div>
        </div>

        <!-- Add more sources -->
        <div class="mt-6 pt-4 border-t border-[#e4e2e4]">
          <button
            type="button"
            class="text-sm text-[#3182CE] hover:text-blue-800 font-medium flex items-center gap-1 transition-colors"
            @click="showSourceBrowser = !showSourceBrowser"
          >
            <span class="material-symbols-outlined text-[16px]">add</span>
            {{ showSourceBrowser ? 'Hide source browser' : 'Browse & add more sources' }}
          </button>
        </div>

        <!-- Source browser -->
        <div v-if="showSourceBrowser" class="mt-4">
          <div class="relative mb-3">
            <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-[#44474d] text-[20px]">search</span>
            <input
              v-model="sourceBrowserQuery"
              type="text"
              class="w-full bg-[#fbf9fb] border border-[#c5c6cd] rounded-lg py-2.5 pl-10 pr-4 text-sm text-[#1b1b1d] focus:outline-none focus:ring-2 focus:ring-[#3182CE] focus:border-transparent placeholder:text-[#75777e]"
              placeholder="Search all available sources..."
            />
          </div>
          <ul class="max-h-60 overflow-y-auto bg-[#fbf9fb] border border-[#c5c6cd] rounded-xl divide-y divide-[#e4e2e4]">
            <li
              v-for="src in filteredBrowseSources"
              :key="src.id"
              class="px-4 py-3 cursor-pointer text-sm flex items-center justify-between hover:bg-[#f5f3f5] transition-colors"
              :class="{ 'bg-blue-50': isSourceSelected(src.id) }"
              @click="toggleSource(src)"
            >
              <div class="flex items-center gap-2">
                <span class="text-xs font-medium uppercase px-2 py-0.5 rounded"
                  :class="sourceTypeBadge(src.type)"
                >{{ src.type }}</span>
                <span>{{ src.name }}</span>
              </div>
              <span v-if="isSourceSelected(src.id)" class="material-symbols-outlined text-[18px] text-[#3182CE]">check</span>
            </li>
            <li v-if="filteredBrowseSources.length === 0" class="px-4 py-6 text-center text-sm text-[#75777e]">No sources found</li>
          </ul>
        </div>
      </div>

      <!-- Period -->
      <div class="flex items-center gap-4">
        <span class="text-sm font-bold text-[#1b1b1d]">Time period:</span>
        <button
          type="button"
          class="px-5 py-2 border rounded-lg text-sm font-medium transition-all"
          :class="days === 7 ? 'bg-black text-white border-black' : 'bg-[#fbf9fb] text-[#1b1b1d] border-[#c5c6cd] hover:border-black'"
          @click="days = 7"
        >7 days</button>
        <button
          type="button"
          class="px-5 py-2 border rounded-lg text-sm font-medium transition-all"
          :class="days === 14 ? 'bg-black text-white border-black' : 'bg-[#fbf9fb] text-[#1b1b1d] border-[#c5c6cd] hover:border-black'"
          @click="days = 14"
        >14 days</button>
        <button
          type="button"
          class="px-5 py-2 border rounded-lg text-sm font-medium transition-all flex items-center gap-2"
          :class="days === 30 ? 'bg-black text-white border-black' : 'bg-[#fbf9fb] text-[#1b1b1d] border-[#c5c6cd] hover:border-black'"
          @click="days = 30"
        >
          30 days
          <span class="text-[10px] font-semibold uppercase tracking-wider px-1.5 py-0.5 rounded"
            :class="days === 30 ? 'bg-white/20 text-white' : 'bg-blue-100 text-blue-700'"
          >rec.</span>
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
            Launching...
          </template>
          <template v-else>
            <span class="material-symbols-outlined icon-fill text-[20px]">auto_awesome</span>
            Launch AI Research
          </template>
        </button>
      </div>
    </main>

    <!-- Footer -->
    <footer class="w-full py-12 px-8 flex flex-col md:flex-row justify-between items-center gap-4 bg-slate-50 border-t border-slate-200">
      <span class="text-lg font-black text-slate-900">InsightArch</span>
      <div class="flex flex-wrap justify-center gap-4">
        <router-link class="text-xs text-slate-500 hover:text-blue-600 transition-colors" to="/terms">Terms</router-link>
        <router-link class="text-xs text-slate-500 hover:text-blue-600 transition-colors" to="/privacy">Privacy</router-link>
        <a class="text-xs text-slate-500 hover:text-blue-600 transition-colors" href="#">Methodology</a>
        <a class="text-xs text-slate-500 hover:text-blue-600 transition-colors" href="#">Support</a>
      </div>
      <p class="text-xs text-slate-500">© 2025 InsightArch Analytics.</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { generateMarketResearch, getExternalTopics } from '../api/graph'

const router = useRouter()

const brief = ref('')
const days = ref(14)
const loading = ref(false)
const aiSelecting = ref(false)
const error = ref('')
const showSourceBrowser = ref(false)
const sourceBrowserQuery = ref('')

// All available sources from backend
const allSources = ref([])

// AI-selected source IDs
const selectedSourceIds = ref([])

// Computed: selected sources
const selectedSources = computed(() => {
  return allSources.value.filter(s => selectedSourceIds.value.includes(s.id))
})

const twitterSources = computed(() => selectedSources.value.filter(s => s.type === 'twitter'))
const redditSources = computed(() => selectedSources.value.filter(s => s.type === 'reddit'))
const telegramSources = computed(() => selectedSources.value.filter(s => s.type === 'telegram'))
const forumSources = computed(() => selectedSources.value.filter(s => s.type === 'forum'))

const filteredBrowseSources = computed(() => {
  if (!sourceBrowserQuery.value) return allSources.value
  const q = sourceBrowserQuery.value.toLowerCase()
  return allSources.value.filter(s => s.name.toLowerCase().includes(q) || s.type.toLowerCase().includes(q))
})

const canSubmit = computed(() => {
  return brief.value.trim() !== '' && selectedSourceIds.value.length > 0
})

function isSourceSelected(id) {
  return selectedSourceIds.value.includes(id)
}

function toggleSource(src) {
  const idx = selectedSourceIds.value.indexOf(src.id)
  if (idx >= 0) {
    selectedSourceIds.value.splice(idx, 1)
  } else {
    selectedSourceIds.value.push(src.id)
  }
}

function removeSource(id) {
  const idx = selectedSourceIds.value.indexOf(id)
  if (idx >= 0) selectedSourceIds.value.splice(idx, 1)
}

function sourceTypeBadge(type) {
  const map = {
    twitter: 'bg-gray-100 text-gray-700',
    reddit: 'bg-orange-100 text-orange-700',
    telegram: 'bg-blue-100 text-blue-700',
    forum: 'bg-emerald-100 text-emerald-700',
  }
  return map[type] || 'bg-gray-100 text-gray-600'
}

async function runAiSelection() {
  if (!brief.value.trim()) return
  aiSelecting.value = true
  error.value = ''
  try {
    const response = await getExternalTopics({ brief: brief.value })
    if (response.success && response.data?.sources) {
      allSources.value = response.data.sources
      // AI pre-selects recommended sources
      const recommended = response.data.recommended_ids || response.data.sources.map(s => s.id)
      selectedSourceIds.value = recommended.slice(0, 20)
    } else {
      error.value = response.error || 'Failed to load sources'
    }
  } catch (err) {
    error.value = err?.response?.data?.error || err?.message || 'Failed to select sources'
  } finally {
    aiSelecting.value = false
  }
}

async function onSubmit() {
  if (!canSubmit.value) return
  loading.value = true
  error.value = ''
  try {
    const response = await generateMarketResearch({
      source_ids: selectedSourceIds.value,
      brief: brief.value,
      days: days.value,
      project_name: `Research: ${brief.value.slice(0, 50)}`,
    })
    if (response.success && response.data?.project_id) {
      router.push({ name: 'Process', params: { projectId: response.data.project_id } })
    } else {
      error.value = response.error || 'Failed to start research'
    }
  } catch (err) {
    error.value = err?.response?.data?.error || err?.message || 'Error starting research'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  // Pre-load all sources for the browser
  getExternalTopics({}).then(res => {
    if (res?.success && res.data?.sources) {
      allSources.value = res.data.sources
    }
  }).catch(() => {})
})
</script>
