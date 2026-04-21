import service, { requestWithRetry } from './index'

/**
 * 生成本体（上传文档和模拟需求）
 * @param {Object} data - 包含files, simulation_requirement, project_name等
 * @returns {Promise}
 */
export function generateOntology(formData) {
  return requestWithRetry(() => 
    service({
      url: '/api/graph/ontology/generate',
      method: 'post',
      data: formData,
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
  )
}

/**
 * Prompt-only mode: generate ontology from prompt without files
 */
export function generateOntologyFromPrompt(data) {
  return requestWithRetry(() =>
    service({
      url: '/api/graph/ontology/generate-from-prompt',
      method: 'post',
      data
    })
  )
}

/**
 * 构建图谱
 * @param {Object} data - 包含project_id, graph_name等
 * @returns {Promise}
 */
export function buildGraph(data) {
  return requestWithRetry(() =>
    service({
      url: '/api/graph/build',
      method: 'post',
      data
    })
  )
}

/**
 * 查询任务状态
 * @param {String} taskId - 任务ID
 * @returns {Promise}
 */
export function getTaskStatus(taskId) {
  return service({
    url: `/api/graph/task/${taskId}`,
    method: 'get'
  })
}

/**
 * 获取图谱数据
 * @param {String} graphId - 图谱ID
 * @returns {Promise}
 */
export function getGraphData(graphId) {
  return service({
    url: `/api/graph/data/${graphId}`,
    method: 'get'
  })
}

/**
 * 获取项目信息
 * @param {String} projectId - 项目ID
 * @returns {Promise}
 */
export function getProject(projectId) {
  return service({
    url: `/api/graph/project/${projectId}`,
    method: 'get'
  })
}

/**
 * Получить список тем из Topic Analyzer (для маркетинговых исследований)
 * @param {String} source - Фильтр: pikabu | habr | vcru | all
 * @param {String} search - Поиск по имени
 * @returns {Promise}
 */
export function getExternalTopics(source = 'all', search = '') {
  return service({
    url: '/api/graph/topics/external',
    method: 'get',
    params: { source, search }
  })
}

/**
 * Запустить маркетинговое исследование (мультиселект тем)
 * @param {Object} data - { topic_ids: [1,5,12], brief: "...", project_name: "..." }
 * @returns {Promise}
 */
export function generateMarketResearch(data) {
  return requestWithRetry(() =>
    service({
      url: '/api/graph/ontology/generate-from-market-research',
      method: 'post',
      data,
      timeout: 600000 // 10 минут — загрузка данных + генерация онтологии
    })
  )
}
