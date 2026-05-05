<template>
  <div class="tw-page bg-[#fbf9fb] text-[#1b1b1d] min-h-screen flex flex-col font-['Inter'] antialiased pt-16">
    <!-- Navbar -->
    <nav class="fixed top-0 left-0 w-full z-50 flex items-center justify-between px-8 h-16 max-w-7xl mx-auto bg-white border-b border-slate-200 shadow-sm right-0">
      <div class="text-xl font-bold text-slate-900 tracking-tight">InsightArch</div>
      <ul class="hidden md:flex space-x-8 items-center h-full">
        <li><a class="text-sm font-medium text-slate-600 hover:text-blue-700 transition-colors cursor-pointer">Dashboard</a></li>
        <li><a class="text-sm font-medium text-slate-600 hover:text-blue-700 transition-colors cursor-pointer">Market Reports</a></li>
        <li><a class="text-sm font-medium text-slate-600 hover:text-blue-700 transition-colors cursor-pointer">Methodology</a></li>
        <li><a class="text-sm font-medium text-slate-600 hover:text-blue-700 transition-colors cursor-pointer">Pricing</a></li>
      </ul>
      <div class="flex items-center space-x-4">
        <button class="text-sm font-medium px-4 py-2 bg-slate-900 text-white rounded-lg hover:opacity-80 transition-opacity" @click="goToResearch">Get Started</button>
      </div>
    </nav>

    <!-- Hero -->
    <section class="max-w-7xl mx-auto px-8 py-16 mt-8">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
        <div class="flex flex-col gap-8">
          <div class="inline-flex items-center gap-2 px-3 py-1 bg-[#efedef] rounded-full border border-[#c5c6cd] w-fit">
            <span class="material-symbols-outlined text-[16px] text-black icon-fill">bolt</span>
            <span class="text-xs font-semibold text-[#44474d] uppercase tracking-wider">NEXT-GENERATION ANALYTICS ENGINE</span>
          </div>
          <h1 class="text-4xl font-bold tracking-tight leading-tight text-[#1b1b1d]">AI market analytics in hours, not weeks.</h1>
          <p class="text-lg text-[#44474d] max-w-xl leading-relaxed">
            Forget slow agencies. Our AI synthesizes data from thousands of up-to-date global and local sources in real time, delivering deep institutional-grade reports.
          </p>
          <div class="flex flex-wrap items-center gap-4 pt-2">
            <button class="bg-black text-white text-base font-medium px-6 py-3 rounded-lg flex items-center gap-2 hover:opacity-90 transition-opacity" @click="goToResearch">
              Start Research
              <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
            </button>
            <button class="bg-transparent text-black border border-[#75777e] text-base font-medium px-6 py-3 rounded-lg flex items-center gap-2 hover:bg-[#efedef] transition-colors">
              Sample Report
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
          <h2 class="text-3xl font-semibold tracking-tight text-[#1b1b1d] mb-2">Institutional rigor, accelerated</h2>
          <p class="text-base text-[#44474d] max-w-2xl mx-auto">Our proprietary AI pipeline transforms fragmented global data into coherent, validated intelligence streams.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="bg-white border border-[#c5c6cd] rounded-xl p-8 flex flex-col gap-4 shadow-[0px_2px_8px_rgba(10,25,47,0.02)] hover:shadow-[0px_8px_24px_rgba(10,25,47,0.06)] transition-shadow">
            <div class="w-12 h-12 bg-[#0d1c32] rounded-lg flex items-center justify-center text-[#76849f]">
              <span class="material-symbols-outlined icon-fill">sensors</span>
            </div>
            <h3 class="text-2xl font-semibold text-[#1b1b1d]">Real-Time Data Collection</h3>
            <p class="text-base text-[#44474d] flex-grow">Analyzes only fresh, dynamically updated sources from the world's best repositories.</p>
          </div>
          <div class="bg-white border border-[#c5c6cd] rounded-xl p-8 flex flex-col gap-4 shadow-[0px_2px_8px_rgba(10,25,47,0.02)] hover:shadow-[0px_8px_24px_rgba(10,25,47,0.06)] transition-shadow">
            <div class="w-12 h-12 bg-[#0d1c32] rounded-lg flex items-center justify-center text-[#76849f]">
              <span class="material-symbols-outlined icon-fill">memory</span>
            </div>
            <h3 class="text-2xl font-semibold text-[#1b1b1d]">Advanced AI Processing</h3>
            <p class="text-base text-[#44474d] flex-grow">Proprietary models cross-verify and validate data to ensure absolute accuracy.</p>
          </div>
          <div class="bg-white border border-[#c5c6cd] rounded-xl p-8 flex flex-col gap-4 shadow-[0px_2px_8px_rgba(10,25,47,0.02)] hover:shadow-[0px_8px_24px_rgba(10,25,47,0.06)] transition-shadow">
            <div class="w-12 h-12 bg-[#0d1c32] rounded-lg flex items-center justify-center text-[#76849f]">
              <span class="material-symbols-outlined icon-fill">lab_profile</span>
            </div>
            <h3 class="text-2xl font-semibold text-[#1b1b1d]">Professional Output</h3>
            <p class="text-base text-[#44474d] flex-grow">Generates board-ready reports with detailed citations, executive summaries, and data matrices.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Pricing -->
    <section class="max-w-7xl mx-auto px-8 py-16">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-semibold tracking-tight text-[#1b1b1d] mb-2">Choose your plan</h2>
        <p class="text-base text-[#44474d] max-w-2xl mx-auto">Institutional-grade market intelligence at a fraction of the cost. Pick the depth that fits your needs.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
        <!-- Plan 1: Market Research $290 -->
        <div class="bg-white border border-[#c5c6cd] rounded-xl p-8 flex flex-col gap-4 shadow-[0px_2px_8px_rgba(10,25,47,0.02)] hover:shadow-[0px_8px_24px_rgba(10,25,47,0.06)] transition-shadow">
          <div class="flex items-center justify-between border-b border-[#c5c6cd] pb-2">
            <h3 class="text-2xl font-semibold text-[#1b1b1d]">Market Research</h3>
            <span class="material-symbols-outlined text-black icon-fill">description</span>
          </div>
          <div class="py-4">
            <span class="text-[40px] font-bold text-[#1b1b1d]">$290</span>
            <span class="text-base text-[#44474d] ml-1">/ report</span>
          </div>
          <ul class="flex flex-col gap-3 mt-2 flex-grow">
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-black mt-0.5 text-[20px]">check</span>
              <span class="text-base text-[#1b1b1d]">Multi-source data synthesis (forums, news, social)</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-black mt-0.5 text-[20px]">check</span>
              <span class="text-base text-[#1b1b1d]">AI-generated knowledge graph</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-black mt-0.5 text-[20px]">check</span>
              <span class="text-base text-[#1b1b1d]">50–80 page professional report</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-black mt-0.5 text-[20px]">check</span>
              <span class="text-base text-[#1b1b1d]">Target audience segmentation</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-black mt-0.5 text-[20px]">check</span>
              <span class="text-base text-[#1b1b1d]">Delivered in 2 hours</span>
            </li>
          </ul>
          <div class="mt-auto pt-8">
            <button class="w-full bg-transparent text-black border border-black text-base font-medium px-6 py-3 rounded-lg hover:bg-[#efedef] transition-colors" @click="goToResearch">Get Started</button>
          </div>
        </div>
        <!-- Plan 2: Research + Market Analysis $490 -->
        <div class="bg-white border border-black rounded-xl p-8 flex flex-col gap-4 relative shadow-[0px_8px_32px_rgba(10,25,47,0.08)]">
          <div class="absolute -top-3 right-8 bg-black text-white text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wider">Recommended</div>
          <div class="flex items-center justify-between border-b border-[#c5c6cd] pb-2">
            <h3 class="text-2xl font-semibold text-[#1b1b1d]">Research + Market Analysis</h3>
            <span class="material-symbols-outlined text-black icon-fill">analytics</span>
          </div>
          <div class="py-4">
            <span class="text-[40px] font-bold text-[#1b1b1d]">$490</span>
            <span class="text-base text-[#44474d] ml-1">/ report</span>
          </div>
          <ul class="flex flex-col gap-3 mt-2 flex-grow">
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-black mt-0.5 text-[20px]">check</span>
              <span class="text-base text-[#1b1b1d]">Everything in Market Research</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-black mt-0.5 text-[20px]">check</span>
              <span class="text-base text-[#1b1b1d]">SWOT analysis for each competitor</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-black mt-0.5 text-[20px]">check</span>
              <span class="text-base text-[#1b1b1d]">Market volume estimation &amp; dynamics</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-black mt-0.5 text-[20px]">check</span>
              <span class="text-base text-[#1b1b1d]">PEST analysis (Political, Economic, Social, Tech)</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-black mt-0.5 text-[20px]">check</span>
              <span class="text-base text-[#1b1b1d]">Multi-agent simulation of market behavior</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="material-symbols-outlined text-black mt-0.5 text-[20px]">check</span>
              <span class="text-base text-[#1b1b1d]">Interactive Q&amp;A with simulated agents</span>
            </li>
          </ul>
          <div class="mt-auto pt-8">
            <button class="w-full bg-black text-white text-base font-medium px-6 py-3 rounded-lg hover:opacity-90 transition-opacity" @click="goToResearch">Get Started</button>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="w-full py-12 px-8 flex flex-col md:flex-row justify-between items-center gap-4 bg-slate-50 border-t border-slate-200">
      <div class="text-lg font-black text-slate-900">InsightArch</div>
      <p class="text-xs text-slate-500">© 2025 InsightArch Analytics. Precision in market intelligence.</p>
      <ul class="flex flex-wrap gap-4 items-center justify-center">
        <li><router-link class="text-xs text-slate-500 hover:text-blue-600 transition-colors" to="/terms">Terms of Service</router-link></li>
        <li><router-link class="text-xs text-slate-500 hover:text-blue-600 transition-colors" to="/privacy">Privacy Policy</router-link></li>
        <li><a class="text-xs text-slate-500 hover:text-blue-600 transition-colors" href="#">Methodology</a></li>
        <li><a class="text-xs text-slate-500 hover:text-blue-600 transition-colors" href="#">Support</a></li>
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
