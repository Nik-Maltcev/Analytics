<template>
  <div class="home-container">
    <!-- Top Navbar -->
    <nav class="navbar">
      <div class="nav-brand">MIROFISH</div>
      <div class="nav-links">
        <a href="https://github.com/666ghj/MiroFish" target="_blank" class="github-link">
          Наш Github <span class="arrow">↗</span>
        </a>
      </div>
    </nav>

    <div class="main-content">
      <!-- Hero Section -->
      <section class="hero-section">
        <div class="hero-left">
          <div class="tag-row">
            <span class="orange-tag">Универсальный движок коллективного интеллекта</span>
            <span class="version-text">/ v0.1-превью</span>
          </div>
          
          <h1 class="main-title">
            Загрузите любой отчёт<br>
            <span class="gradient-text">Смоделируйте будущее</span>
          </h1>
          
          <div class="hero-desc">
            <p>
              Даже из одного абзаца текста <span class="highlight-bold">MiroFish</span> извлечёт реальные зёрна и автоматически создаст параллельный мир из до <span class="highlight-orange">миллиона агентов</span>. Внедряйте переменные с позиции наблюдателя и находите <span class="highlight-code">«локальный оптимум»</span> в сложных групповых взаимодействиях
            </p>
            <p class="slogan-text">
              Пусть будущее разыграется среди агентов, а решения победят после сотен битв<span class="blinking-cursor">_</span>
            </p>
          </div>
           
          <div class="decoration-square"></div>
        </div>
        
        <div class="hero-right">
          <!-- Logo Area -->
          <div class="logo-container">
            <img src="../assets/logo/MiroFish_logo_left.jpeg" alt="MiroFish Logo" class="hero-logo" />
          </div>
          
          <button class="scroll-down-btn" @click="scrollToBottom">
            ↓
          </button>
        </div>
      </section>

      <!-- Two-Column Layout -->
      <section class="dashboard-section">
        <!-- Left: Status & Steps -->
        <div class="left-panel">
          <div class="panel-header">
            <span class="status-dot">■</span> Статус системы
          </div>
          
          <h2 class="section-title">Готов к работе</h2>
          <p class="section-desc">
            Движок прогнозирования в режиме ожидания. Загрузите неструктурированные данные для инициализации симуляции
          </p>
          
          <!-- Metrics Cards -->
          <div class="metrics-row">
            <div class="metric-card">
              <div class="metric-value">Низкая цена</div>
              <div class="metric-label">В среднем ~5$ за симуляцию</div>
            </div>
            <div class="metric-card">
              <div class="metric-value">Масштаб</div>
              <div class="metric-label">До миллиона агентов</div>
            </div>
          </div>

          <!-- Simulation Steps -->
          <div class="steps-container">
            <div class="steps-header">
               <span class="diamond-icon">◇</span> Рабочий процесс
            </div>
            <div class="workflow-list">
              <div class="workflow-item">
                <span class="step-num">01</span>
                <div class="step-info">
                  <div class="step-title">Построение графа</div>
                  <div class="step-desc">Извлечение реальных зёрен & внедрение памяти & построение GraphRAG</div>
                </div>
              </div>
              <div class="workflow-item">
                <span class="step-num">02</span>
                <div class="step-info">
                  <div class="step-title">Настройка среды</div>
                  <div class="step-desc">Извлечение сущностей & генерация профилей & настройка параметров агентов</div>
                </div>
              </div>
              <div class="workflow-item">
                <span class="step-num">03</span>
                <div class="step-info">
                  <div class="step-title">Запуск симуляции</div>
                  <div class="step-desc">Параллельная симуляция на двух платформах & динамическое обновление памяти</div>
                </div>
              </div>
              <div class="workflow-item">
                <span class="step-num">04</span>
                <div class="step-info">
                  <div class="step-title">Генерация отчёта</div>
                  <div class="step-desc">ReportAgent с набором инструментов для глубокого анализа результатов</div>
                </div>
              </div>
              <div class="workflow-item">
                <span class="step-num">05</span>
                <div class="step-info">
                  <div class="step-title">Глубокое взаимодействие</div>
                  <div class="step-desc">Диалог с любым агентом мира & общение с ReportAgent</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right: Console -->
        <div class="right-panel">
          <div class="console-box">
            <!-- Mode Switcher -->
            <div class="console-section">
              <div class="mode-switcher">
                <button 
                  class="mode-btn" 
                  :class="{ active: workMode === 'market_research' }"
                  @click="workMode = 'market_research'"
                >
                  📊 Маркетинговое исследование
                </button>
                <button 
                  class="mode-btn" 
                  :class="{ active: workMode === 'prediction' }"
                  @click="workMode = 'prediction'"
                >
                  🔮 Прогнозирование
                </button>
              </div>
            </div>

            <!-- ═══ Market Research Mode ═══ -->
            <template v-if="workMode === 'market_research'">
              <div class="console-section">
                <div class="console-header">
                  <span class="console-label">01 / Выбор тем (1-5)</span>
                  <span class="console-meta">{{ selectedTopicIds.length }}/5 выбрано</span>
                </div>
                
                <!-- Период -->
                <div class="period-selector">
                  <span class="period-label">Период:</span>
                  <button v-for="d in [7, 14, 30]" :key="d"
                    class="period-btn" :class="{ active: days === d }"
                    @click="days = d">{{ d }} дней</button>
                </div>
                
                <div v-if="topicsLoading" class="topics-loading">
                  Загрузка тем из Topic Analyzer...
                </div>
                <div v-else-if="topicsError" class="topics-error">
                  {{ topicsError }}
                  <button class="retry-btn" @click="loadExternalTopics">Повторить</button>
                </div>
                <div v-else class="topics-selector">
                  <div v-for="(topics, source) in groupedTopics" :key="source" class="source-group">
                    <div class="source-header">{{ sourceLabels[source] || source }}</div>
                    <div class="topics-grid">
                      <button
                        v-for="topic in topics"
                        :key="topic.id"
                        class="topic-chip"
                        :class="{ selected: isTopicSelected(topic.id), disabled: !isTopicSelected(topic.id) && selectedTopicIds.length >= 5 }"
                        @click="toggleTopic(topic.id)"
                        :disabled="!isTopicSelected(topic.id) && selectedTopicIds.length >= 5"
                      >
                        {{ topic.name }}
                      </button>
                    </div>
                  </div>
                </div>
              </div>

              <div class="console-divider"><span>Бриф клиента</span></div>

              <div class="console-section">
                <div class="console-header">
                  <span class="console-label">>_ 02 / Описание задачи</span>
                </div>
                <div class="input-wrapper">
                  <textarea
                    v-model="brief"
                    class="code-input"
                    placeholder="// Опишите задачу клиента: ниша, продукт, что нужно исследовать"
                    rows="4"
                    :disabled="loading"
                  ></textarea>
                  <div class="model-badge">Режим: Market Research</div>
                </div>
              </div>
            </template>

            <!-- ═══ Prediction Mode (existing) ═══ -->
            <template v-else>
              <!-- Upload Area -->
              <div class="console-section">
                <div class="console-header">
                  <span class="console-label">01 / Исходные данные</span>
                  <span class="console-meta">
                    <label class="mode-toggle">
                      <input type="checkbox" v-model="promptOnlyMode" :disabled="loading">
                      <span class="toggle-label">{{ promptOnlyMode ? 'Только промпт' : 'С документами' }}</span>
                    </label>
                  </span>
                </div>
                
                <div v-if="!promptOnlyMode"
                  class="upload-zone"
                  :class="{ 'drag-over': isDragOver, 'has-files': files.length > 0 }"
                  @dragover.prevent="handleDragOver"
                  @dragleave.prevent="handleDragLeave"
                  @drop.prevent="handleDrop"
                  @click="triggerFileInput"
                >
                  <input
                    ref="fileInput"
                    type="file"
                    multiple
                    accept=".pdf,.md,.txt"
                    @change="handleFileSelect"
                    style="display: none"
                    :disabled="loading"
                  />
                  
                  <div v-if="files.length === 0" class="upload-placeholder">
                    <div class="upload-icon">↑</div>
                    <div class="upload-title">Перетащите файлы сюда</div>
                    <div class="upload-hint">или нажмите для выбора • PDF, MD, TXT</div>
                  </div>
                  
                  <div v-else class="file-list">
                    <div v-for="(file, index) in files" :key="index" class="file-item">
                      <span class="file-icon">📄</span>
                      <span class="file-name">{{ file.name }}</span>
                      <button @click.stop="removeFile(index)" class="remove-btn">×</button>
                    </div>
                  </div>
                </div>
                
                <div v-else class="prompt-only-hint">
                  <div class="hint-icon">⚡</div>
                  <div class="hint-text">LLM сгенерирует сценарий из вашего промпта</div>
                  <div class="hint-sub">Документы не нужны — AI создаст контекст автоматически</div>
                </div>
              </div>

              <div class="console-divider"><span>Параметры</span></div>

              <div class="console-section">
                <div class="console-header">
                  <span class="console-label">>_ 02 / Промпт симуляции</span>
                </div>
                <div class="input-wrapper">
                  <textarea
                    v-model="formData.simulationRequirement"
                    class="code-input"
                    placeholder="// Опишите на естественном языке, что нужно смоделировать или спрогнозировать"
                    rows="6"
                    :disabled="loading"
                  ></textarea>
                  <div class="model-badge">Движок: MiroFish-V1.0</div>
                </div>
              </div>
            </template>

            <!-- Error -->
            <div v-if="error" class="console-section error-section">
              <div class="error-msg">{{ error }}</div>
            </div>

            <!-- Start Button -->
            <div class="console-section btn-section">
              <button 
                class="start-engine-btn"
                @click="startSimulation"
                :disabled="!canSubmit || loading"
              >
                <span v-if="!loading">
                  {{ workMode === 'market_research' ? 'Запустить исследование' : 'Запустить' }}
                </span>
                <span v-else>Инициализация...</span>
                <span class="btn-arrow">→</span>
              </button>
            </div>
          </div>
        </div>
      </section>

      <!-- History Database -->
      <HistoryDatabase />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import HistoryDatabase from '../components/HistoryDatabase.vue'
import { getExternalTopics, generateMarketResearch } from '../api/graph'

const router = useRouter()

// ═══ Режим работы ═══
const workMode = ref('market_research') // 'market_research' | 'prediction'

// ═══ Market Research: темы из Topic Analyzer ═══
const externalTopics = ref([])       // Все темы
const groupedTopics = ref({})        // Сгруппированные по источнику
const selectedTopicIds = ref([])     // Выбранные topic_id
const days = ref(30)                 // Период: 7 | 14 | 30
const topicsLoading = ref(false)
const topicsError = ref('')

// Загрузка тем из Topic Analyzer
const loadExternalTopics = async () => {
  topicsLoading.value = true
  topicsError.value = ''
  try {
    const response = await getExternalTopics('all')
    if (response.success) {
      externalTopics.value = response.data.topics || []
      groupedTopics.value = response.data.grouped || {}
    } else {
      topicsError.value = response.error || 'Ошибка загрузки тем'
    }
  } catch (err) {
    topicsError.value = 'Topic Analyzer недоступен. Проверьте подключение.'
  } finally {
    topicsLoading.value = false
  }
}

// Переключение выбора темы
const toggleTopic = (topicId) => {
  const idx = selectedTopicIds.value.indexOf(topicId)
  if (idx >= 0) {
    selectedTopicIds.value.splice(idx, 1)
  } else if (selectedTopicIds.value.length < 5) {
    selectedTopicIds.value.push(topicId)
  }
}

const isTopicSelected = (topicId) => selectedTopicIds.value.includes(topicId)

// Человекочитаемые названия источников
const sourceLabels = { pikabu: 'Pikabu', habr: 'Habr', vcru: 'VC.ru' }

// ═══ Prediction mode (существующий) ═══
const formData = ref({ simulationRequirement: '' })
const files = ref([])
const loading = ref(false)
const error = ref('')
const isDragOver = ref(false)
const fileInput = ref(null)
const promptOnlyMode = ref(false)

// ═══ Общий бриф (используется в обоих режимах) ═══
const brief = ref('')

// ═══ Computed ═══
const canSubmit = computed(() => {
  if (workMode.value === 'market_research') {
    return selectedTopicIds.value.length > 0 && brief.value.trim() !== ''
  }
  // prediction mode
  if (promptOnlyMode.value) {
    return formData.value.simulationRequirement.trim() !== ''
  }
  return formData.value.simulationRequirement.trim() !== '' && files.value.length > 0
})

// ═══ Lifecycle ═══
onMounted(() => {
  loadExternalTopics()
})

watch(workMode, (newMode) => {
  if (newMode === 'market_research' && externalTopics.value.length === 0) {
    loadExternalTopics()
  }
})

// ═══ File handling (prediction mode) ═══
const triggerFileInput = () => { if (!loading.value) fileInput.value?.click() }
const handleFileSelect = (event) => addFiles(Array.from(event.target.files))
const handleDragOver = () => { if (!loading.value) isDragOver.value = true }
const handleDragLeave = () => { isDragOver.value = false }
const handleDrop = (e) => {
  isDragOver.value = false
  if (!loading.value) addFiles(Array.from(e.dataTransfer.files))
}
const addFiles = (newFiles) => {
  files.value.push(...newFiles.filter(f => ['pdf','md','txt'].includes(f.name.split('.').pop().toLowerCase())))
}
const removeFile = (index) => { files.value.splice(index, 1) }

const scrollToBottom = () => {
  window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })
}

// ═══ Start ═══
const startSimulation = async () => {
  if (!canSubmit.value || loading.value) return

  if (workMode.value === 'market_research') {
    // Маркетинговое исследование
    loading.value = true
    error.value = ''
    try {
      const response = await generateMarketResearch({
        topic_ids: selectedTopicIds.value,
        brief: brief.value,
        days: days.value,
        project_name: `Research: ${brief.value.substring(0, 50)}`,
      })
      if (response.success && response.data?.project_id) {
        router.push({
          name: 'Process',
          params: { projectId: response.data.project_id }
        })
      } else {
        error.value = response.error || 'Ошибка создания исследования'
      }
    } catch (err) {
      error.value = err.message || 'Ошибка подключения'
    } finally {
      loading.value = false
    }
  } else {
    // Prediction mode (существующий)
    import('../store/pendingUpload.js').then(({ setPendingUpload }) => {
      setPendingUpload(
        promptOnlyMode.value ? [] : files.value,
        formData.value.simulationRequirement,
        promptOnlyMode.value
      )
      router.push({ name: 'Process', params: { projectId: 'new' } })
    })
  }
}
</script>

<style scoped>
/* Global vars & reset */
:root {
  --black: #000000;
  --white: #FFFFFF;
  --orange: #FF4500;
  --gray-light: #F5F5F5;
  --gray-text: #666666;
  --border: #E5E5E5;
  /* 
    Space Grotesk for headings, JetBrains Mono for code
    Ensure Google Fonts are imported in index.html 
  */
  --font-mono: 'JetBrains Mono', monospace;
  --font-sans: 'Space Grotesk', 'Noto Sans SC', system-ui, sans-serif;
  --font-cn: 'Noto Sans SC', system-ui, sans-serif;
}

.home-container {
  min-height: 100vh;
  background: var(--white);
  font-family: var(--font-sans);
  color: var(--black);
}

/* Top Navbar */
.navbar {
  height: 60px;
  background: var(--black);
  color: var(--white);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 40px;
}

.nav-brand {
  font-family: var(--font-mono);
  font-weight: 800;
  letter-spacing: 1px;
  font-size: 1.2rem;
}

.nav-links {
  display: flex;
  align-items: center;
}

.github-link {
  color: var(--white);
  text-decoration: none;
  font-family: var(--font-mono);
  font-size: 0.9rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: opacity 0.2s;
}

.github-link:hover {
  opacity: 0.8;
}

.arrow {
  font-family: sans-serif;
}

/* Main Content */
.main-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 60px 40px;
}

/* Hero Section */
.hero-section {
  display: flex;
  justify-content: space-between;
  margin-bottom: 80px;
  position: relative;
}

.hero-left {
  flex: 1;
  padding-right: 60px;
}

.tag-row {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 25px;
  font-family: var(--font-mono);
  font-size: 0.8rem;
}

.orange-tag {
  background: var(--orange);
  color: var(--white);
  padding: 4px 10px;
  font-weight: 700;
  letter-spacing: 1px;
  font-size: 0.75rem;
}

.version-text {
  color: #999;
  font-weight: 500;
  letter-spacing: 0.5px;
}

.main-title {
  font-size: 4.5rem;
  line-height: 1.2;
  font-weight: 500;
  margin: 0 0 40px 0;
  letter-spacing: -2px;
  color: var(--black);
}

.gradient-text {
  background: linear-gradient(90deg, #000000 0%, #444444 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}

.hero-desc {
  font-size: 1.05rem;
  line-height: 1.8;
  color: var(--gray-text);
  max-width: 640px;
  margin-bottom: 50px;
  font-weight: 400;
  text-align: justify;
}

.hero-desc p {
  margin-bottom: 1.5rem;
}

.highlight-bold {
  color: var(--black);
  font-weight: 700;
}

.highlight-orange {
  color: var(--orange);
  font-weight: 700;
  font-family: var(--font-mono);
}

.highlight-code {
  background: rgba(0, 0, 0, 0.05);
  padding: 2px 6px;
  border-radius: 2px;
  font-family: var(--font-mono);
  font-size: 0.9em;
  color: var(--black);
  font-weight: 600;
}

.slogan-text {
  font-size: 1.2rem;
  font-weight: 520;
  color: var(--black);
  letter-spacing: 1px;
  border-left: 3px solid var(--orange);
  padding-left: 15px;
  margin-top: 20px;
}

.blinking-cursor {
  color: var(--orange);
  animation: blink 1s step-end infinite;
  font-weight: 700;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

.decoration-square {
  width: 16px;
  height: 16px;
  background: var(--orange);
}

.hero-right {
  flex: 0.8;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-end;
}

.logo-container {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  padding-right: 40px;
}

.hero-logo {
  max-width: 500px; /* Logo size */
  width: 100%;
}

.scroll-down-btn {
  width: 40px;
  height: 40px;
  border: 1px solid var(--border);
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--orange);
  font-size: 1.2rem;
  transition: all 0.2s;
}

.scroll-down-btn:hover {
  border-color: var(--orange);
}

/* Dashboard Two-Column Layout */
.dashboard-section {
  display: flex;
  gap: 60px;
  border-top: 1px solid var(--border);
  padding-top: 60px;
  align-items: flex-start;
}

.dashboard-section .left-panel,
.dashboard-section .right-panel {
  display: flex;
  flex-direction: column;
}

/* Left Panel */
.left-panel {
  flex: 0.8;
}

.panel-header {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: #999;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 20px;
}

.status-dot {
  color: var(--orange);
  font-size: 0.8rem;
}

.section-title {
  font-size: 2rem;
  font-weight: 520;
  margin: 0 0 15px 0;
}

.section-desc {
  color: var(--gray-text);
  margin-bottom: 25px;
  line-height: 1.6;
}

.metrics-row {
  display: flex;
  gap: 20px;
  margin-bottom: 15px;
}

.metric-card {
  border: 1px solid var(--border);
  padding: 20px 30px;
  min-width: 150px;
}

.metric-value {
  font-family: var(--font-mono);
  font-size: 1.8rem;
  font-weight: 520;
  margin-bottom: 5px;
}

.metric-label {
  font-size: 0.85rem;
  color: #999;
}

/* Simulation Steps */
.steps-container {
  border: 1px solid var(--border);
  padding: 30px;
  position: relative;
}

.steps-header {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: #999;
  margin-bottom: 25px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.diamond-icon {
  font-size: 1.2rem;
  line-height: 1;
}

.workflow-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.workflow-item {
  display: flex;
  align-items: flex-start;
  gap: 20px;
}

.step-num {
  font-family: var(--font-mono);
  font-weight: 700;
  color: var(--black);
  opacity: 0.3;
}

.step-info {
  flex: 1;
}

.step-title {
  font-weight: 520;
  font-size: 1rem;
  margin-bottom: 4px;
}

.step-desc {
  font-size: 0.85rem;
  color: var(--gray-text);
}

/* Right Console */
.right-panel {
  flex: 1.2;
}

.console-box {
  border: 1px solid #CCC; /* outer border */
  padding: 8px; /* padding for double border effect */
}

.console-section {
  padding: 20px;
}

.console-section.btn-section {
  padding-top: 0;
}

.console-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 15px;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: #666;
}

.upload-zone {
  border: 1px dashed #CCC;
  height: 200px;
  overflow-y: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s;
  background: #FAFAFA;
}

.upload-zone.has-files {
  align-items: flex-start;
}

.upload-zone:hover {
  background: #F0F0F0;
  border-color: #999;
}

/* Mode toggle */
.mode-toggle {
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  user-select: none;
}

.mode-toggle input {
  accent-color: #FF4500;
  cursor: pointer;
}

.toggle-label {
  font-size: 0.75rem;
  color: #666;
}

/* Prompt-only hint */
.prompt-only-hint {
  border: 1px dashed #FF4500;
  height: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: #FFF8F5;
  gap: 8px;
}

.hint-icon {
  font-size: 2rem;
}

.hint-text {
  font-size: 0.9rem;
  font-weight: 600;
  color: #333;
}

.hint-sub {
  font-size: 0.75rem;
  color: #999;
}

.upload-placeholder {
  text-align: center;
}

.upload-icon {
  width: 40px;
  height: 40px;
  border: 1px solid #DDD;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 15px;
  color: #999;
}

.upload-title {
  font-weight: 500;
  font-size: 0.9rem;
  margin-bottom: 5px;
}

.upload-hint {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: #999;
}

.file-list {
  width: 100%;
  padding: 15px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.file-item {
  display: flex;
  align-items: center;
  background: var(--white);
  padding: 8px 12px;
  border: 1px solid #EEE;
  font-family: var(--font-mono);
  font-size: 0.85rem;
}

.file-name {
  flex: 1;
  margin: 0 10px;
}

.remove-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.2rem;
  color: #999;
}

.console-divider {
  display: flex;
  align-items: center;
  margin: 10px 0;
}

.console-divider::before,
.console-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: #EEE;
}

.console-divider span {
  padding: 0 15px;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: #BBB;
  letter-spacing: 1px;
}

.input-wrapper {
  position: relative;
  border: 1px solid #DDD;
  background: #FAFAFA;
}

.code-input {
  width: 100%;
  border: none;
  background: transparent;
  padding: 20px;
  font-family: var(--font-mono);
  font-size: 0.9rem;
  line-height: 1.6;
  resize: vertical;
  outline: none;
  min-height: 150px;
}

.model-badge {
  position: absolute;
  bottom: 10px;
  right: 15px;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: #AAA;
}

.start-engine-btn {
  width: 100%;
  background: var(--black);
  color: var(--white);
  border: none;
  padding: 20px;
  font-family: var(--font-mono);
  font-weight: 700;
  font-size: 1.1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  letter-spacing: 1px;
  position: relative;
  overflow: hidden;
}

/* Clickable state (not disabled) */
.start-engine-btn:not(:disabled) {
  background: var(--black);
  border: 1px solid var(--black);
  animation: pulse-border 2s infinite;
}

.start-engine-btn:hover:not(:disabled) {
  background: var(--orange);
  border-color: var(--orange);
  transform: translateY(-2px);
}

.start-engine-btn:active:not(:disabled) {
  transform: translateY(0);
}

.start-engine-btn:disabled {
  background: #E5E5E5;
  color: #999;
  cursor: not-allowed;
  transform: none;
  border: 1px solid #E5E5E5;
}

/* Guide animation: subtle border pulse */
@keyframes pulse-border {
  0% { box-shadow: 0 0 0 0 rgba(0, 0, 0, 0.2); }
  70% { box-shadow: 0 0 0 6px rgba(0, 0, 0, 0); }
  100% { box-shadow: 0 0 0 0 rgba(0, 0, 0, 0); }
}

/* 响应式适配 */
@media (max-width: 1024px) {
  .dashboard-section {
    flex-direction: column;
  }
  
  .hero-section {
    flex-direction: column;
  }
  
  .hero-left {
    padding-right: 0;
    margin-bottom: 40px;
  }
  
  .hero-logo {
    max-width: 200px;
    margin-bottom: 20px;
  }
}

/* ═══ Mode Switcher ═══ */
.mode-switcher {
  display: flex;
  gap: 8px;
  margin-bottom: 8px;
}
.mode-btn {
  flex: 1;
  padding: 10px 16px;
  border: 1px solid #333;
  background: transparent;
  color: #888;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}
.mode-btn.active {
  background: #1a1a1a;
  color: #fff;
  border-color: #FF6B35;
}
.mode-btn:hover:not(.active) {
  border-color: #555;
  color: #ccc;
}

/* ═══ Topics Selector ═══ */
.period-selector {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
}
.period-label {
  font-size: 12px;
  color: #888;
}
.period-btn {
  padding: 4px 12px;
  border: 1px solid #333;
  background: transparent;
  color: #aaa;
  font-size: 12px;
  cursor: pointer;
  font-family: inherit;
  transition: all 0.15s;
}
.period-btn.active {
  background: #FF6B35;
  border-color: #FF6B35;
  color: #000;
  font-weight: 600;
}
.period-btn:hover:not(.active) {
  border-color: #555;
  color: #fff;
}
.topics-loading, .topics-error {
  padding: 20px;
  text-align: center;
  color: #888;
  font-size: 13px;
}
.topics-error { color: #C5283D; }
.retry-btn {
  margin-top: 8px;
  padding: 4px 12px;
  background: transparent;
  border: 1px solid #555;
  color: #ccc;
  cursor: pointer;
  font-size: 12px;
}
.source-group { margin-bottom: 12px; }
.source-header {
  font-size: 11px;
  color: #FF6B35;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 6px;
  padding-left: 2px;
}
.topics-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.topic-chip {
  padding: 5px 12px;
  border: 1px solid #333;
  background: transparent;
  color: #aaa;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.15s;
  font-family: inherit;
}
.topic-chip:hover:not(.disabled) {
  border-color: #FF6B35;
  color: #fff;
}
.topic-chip.selected {
  background: #FF6B35;
  border-color: #FF6B35;
  color: #000;
  font-weight: 600;
}
.topic-chip.disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.error-section { margin-top: 8px; }
.error-msg {
  color: #C5283D;
  font-size: 13px;
  padding: 8px 12px;
  border: 1px solid #C5283D33;
  background: #C5283D11;
}
</style>
