import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const tests = ref([
    {id:1, title:'title1', content:'content1'},{id:2, title:'title2', content:'content2'}
  ])
  return { tests }
})
