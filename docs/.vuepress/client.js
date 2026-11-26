import { defineClientConfig } from 'vuepress/client'
import SectionGrid from './components/SectionGrid.vue'
import Quiz from './components/Quiz.vue'
import Mindmap from './components/Mindmap.vue'
import { setupReviewJumps } from './lib/review-jump.js'

export default defineClientConfig({
  enhance({ app, router }) {
    app.component('SectionGrid', SectionGrid)
    app.component('Quiz', Quiz)
    app.component('Mindmap', Mindmap)
    if (__VUEPRESS_DEV__) setupReviewJumps(router)
  },
})
