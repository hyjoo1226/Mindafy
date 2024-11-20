import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
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
  // const tests = ref([])
  // const API_URL = 'http://127.0.0.1:8000'

  // const getTests = function(){
  //   axios({
  //     method:'get',
  //     url:`${API_URL}/api/v1/tests/`
  //   })
  //     .then(res => {
  //       tests.value = res.data
  //     })
  //     .catch(err => console.log(err))
  // }

  const TestIdToTest = function(testId){
    const intTestId = Number(testId)
    for(let test of tests.value){
      if(test.id === intTestId){    
        return test
      }
    }
  }
  // const signUp = function(payload){
  //     const username = payload.username
  //     const password1 = payload.password1
  //     const password2 = payload.password2

  //     axios({
  //       method:'post',
  //       url:`${API_URL}/accouts/signup/`,
  //       data: {
  //         username, password1, password2
  //       }
  //     })
  //       .then(res => {
  //         console.log('회원가입이 완료되었습니다.');
  //       })
  //       .catch(err => 
  //         console.log(err))
  // }
  // const token = ref(null)
  // const logIn = function(){
  //   const username = payload.username
  //   const password = payload.password
  //   axios({
  //     method:'post',
  //     url:`${API_URL}/accouts/login/`,
  //     data: {
  //       username, password
  //     }
  //   })
  //     .then(res => {
  //       console.log('로그인이 완료되었습니다.');
  //       token.value = res.data.key
        
  //     })
  //     .catch(err => console.log(err))
  // }
  
  
  return { tests, TestIdToTest, API_URL, getTests,  signUp, logIn, token }
}, {persist: true})

