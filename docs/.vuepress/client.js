import { defineClientConfig } from 'vuepress/client'
import SectionGrid from './components/SectionGrid.vue'
import Quiz from './components/Quiz.vue'
import Mindmap from './components/Mindmap.vue'

export default defineClientConfig({
  enhance({ app }) {
    app.component('SectionGrid', SectionGrid)
    app.component('Quiz', Quiz)
    app.component('Mindmap', Mindmap)
  },
})
