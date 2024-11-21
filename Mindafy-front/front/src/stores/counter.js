//counter.js
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router';
export const useCounterStore = defineStore('counter', () => {
  const tests = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  const getTests = function(){
    axios({
      method:'get',
      url:`${API_URL}/api/v1/tests/`
    })
      .then(res => {
        tests.value = res.data
      })
      .catch(err => console.log(err))
  }

  const token = ref(null)
  const logIn = function(payload){
    const username = payload.username
    const password = payload.password
    axios({
      method:'post',
      url:`${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
    .then(res => {
      console.log('로그인이 완료되었습니다.');
      token.value = res.data.key
      router.push({name:'test'})
      console.log(res);
      
    })
    .catch(err => console.log(err))
  }
  
  const signUp = function(payload){
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      const nickname = payload.nickname
      const age = payload.age
      const email = payload.email
      const profile_img = payload.profile_img
      
      axios({
        method:'post',
        url:`${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2, nickname, age, email, profile_img
        }
      })
        .then(res => {
          console.log('회원가입이 완료되었습니다.');
          const password = password1
          logIn({username, password})
        })
        .catch((err) => {
          console.log(err)
          alert('입력 정보를 다시 확인해 주세요.')
        });
  }
  
  const logOut = function() {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      headers: {
        Authorization: `Token ${token.value}`, // 인증 토큰 포함
      },
    })
      .then(() => {
        token.value = null; // 토큰 제거
        router.push({ name: 'login' }); // 로그인 페이지로 이동
        console.log('로그아웃이 완료되었습니다.');
      })
      .catch(err => {
        console.error('로그아웃 요청 중 오류 발생:', err);
      });
  };
  
  
  
  return { tests, API_URL, getTests, signUp, logIn, token,logOut }
}, {persist: true})

