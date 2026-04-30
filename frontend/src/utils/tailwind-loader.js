/**
 * Dynamically loads Tailwind CSS CDN + config.
 * Call in onMounted() of pages that need Tailwind.
 * Removes itself in onUnmounted() to avoid polluting other pages.
 */

const TAILWIND_CONFIG = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "surface-container-high": "#eae7ea",
        "on-error-container": "#93000a",
        "primary": "#000000",
        "surface-container-lowest": "#ffffff",
        "primary-container": "#0d1c32",
        "outline-variant": "#c5c6cd",
        "surface-dim": "#dbd9db",
        "secondary": "#555f71",
        "surface-container-low": "#f5f3f5",
        "on-secondary": "#ffffff",
        "surface": "#fbf9fb",
        "on-tertiary": "#ffffff",
        "surface-container-highest": "#e4e2e4",
        "on-background": "#1b1b1d",
        "primary-fixed": "#d6e3ff",
        "primary-fixed-dim": "#b9c7e4",
        "background": "#fbf9fb",
        "surface-variant": "#e4e2e4",
        "on-error": "#ffffff",
        "on-primary-container": "#76849f",
        "outline": "#75777e",
        "error": "#ba1a1a",
        "surface-container": "#efedef",
        "on-primary": "#ffffff",
        "on-surface": "#1b1b1d",
        "on-surface-variant": "#44474d"
      },
    }
  }
}

let scriptEl = null
let refCount = 0

export function loadTailwind() {
  refCount++
  if (scriptEl) return

  // Set config before loading script
  window.tailwind = { config: TAILWIND_CONFIG }

  scriptEl = document.createElement('script')
  scriptEl.src = 'https://cdn.tailwindcss.com?plugins=forms,container-queries'
  scriptEl.id = 'tailwind-cdn'
  document.head.appendChild(scriptEl)
}

export function unloadTailwind() {
  refCount--
  if (refCount <= 0 && scriptEl) {
    scriptEl.remove()
    scriptEl = null
    refCount = 0
    // Remove tailwind generated style
    const twStyle = document.querySelector('style[data-tailwind]') ||
                    document.getElementById('_tailwind') ||
                    document.querySelector('style:last-of-type')
    // Don't remove — it's harmless and removing can cause flicker
  }
}
