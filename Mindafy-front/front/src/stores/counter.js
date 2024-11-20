import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const tests = ref([
    {
      id: 1,
      title: "title1",
      description: "description1",
      participant_count: 0,
      duration: 5,
      test_img: "string",
      created_at: "datetime",
      updated_at: "datetime",
      recommendation_count: 0,
      result: "result1"
     },
     {
      id: 2,
      title: "title2",
      description: "description2",
      participant_count: 0,
      duration: 5,
      test_img: "string",
      created_at: "datetime",
      updated_at: "datetime",
      recommendation_count: 0,
      result: "result2"
     },
  ])
  const TestIdToTest = function(testId){
    const intTestId = Number(testId)
    for(let test of tests.value){
      if(test.id === intTestId){    
        return test
      }
    }
  }
  return { tests, TestIdToTest }
})
