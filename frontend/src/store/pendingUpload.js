/**
 * Temporary store for pending upload data.
 * Used when navigating from Home to Process page.
 */
import { reactive } from 'vue'

const state = reactive({
  files: [],
  simulationRequirement: '',
  isPending: false,
  promptOnly: false
})

export function setPendingUpload(files, requirement, promptOnly = false) {
  state.files = files
  state.simulationRequirement = requirement
  state.isPending = true
  state.promptOnly = promptOnly
}

export function getPendingUpload() {
  return {
    files: state.files,
    simulationRequirement: state.simulationRequirement,
    isPending: state.isPending,
    promptOnly: state.promptOnly
  }
}

export function clearPendingUpload() {
  state.files = []
  state.simulationRequirement = ''
  state.isPending = false
  state.promptOnly = false
}

export default state
