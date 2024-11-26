import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router';

export const useCounterStore = defineStore('counter', () => {
  const tests = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  const user = ref(null)
  const token = ref(null)
  const testResult = ref(null)  // 테스트 결과를 저장할 상태 추가

  // 기존 함수들...
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
      console.log(res.data.user);
      user.value = res.data.user
      router.push({name:'test'})
    })
    .catch((err)=>{
      console.log(err)
      alert('id와 password를 확인해주세요')
    })
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
        Authorization: `Token ${token.value}`,
      },
    })
      .then(() => {
        token.value = null;
        user.value = null
        testResult.value = null  // 로그아웃 시 테스트 결과도 초기화
        router.push({ name: 'login' });
        console.log('로그아웃이 완료되었습니다.');
      })
      .catch(err => {
        console.error('로그아웃 요청 중 오류 발생:', err);
      });
  };

  const updateProfile = async function (payload) {
    try {
      if (payload.old_password && payload.new_password1 && payload.new_password2) {
        const passwordResponse = await axios({
          method: 'post',
          url: `${API_URL}/accounts/password/change/`,
          headers: {
            Authorization: `Token ${token.value}`,
          },
          data: {
            old_password: payload.old_password,
            new_password1: payload.new_password1,
            new_password2: payload.new_password2,
          },
        });
        console.log('Password updated:', passwordResponse.data);
      }

      if (payload.nickname) {
        const nicknameResponse = await axios({
          method: 'patch',
          url: `${API_URL}/accounts/users/${user.value.id}/nickname/`,
          headers: {
            Authorization: `Token ${token.value}`,
          },
          data: { nickname: payload.nickname },
        });
        console.log('Nickname updated:', nicknameResponse.data);
      }

      if (payload.profile_img) {
        const profileImgResponse = await axios({
          method: 'patch',
          url: `${API_URL}/accounts/users/${user.value.id}/profile_img/`,
          headers: {
            Authorization: `Token ${token.value}`,
          },
          data: { profile_img: payload.profile_img },
        });
        console.log('Profile image updated:', profileImgResponse.data);
      }

      user.value = { ...user.value, ...payload };
      console.log('Profile updated:', user.value);
    } catch (err) {
      console.error('Error updating profile:', err);
      alert('Failed to update profile.');
      throw err;
    }
  };

  // 테스트 결과 관련 새로운 함수들 추가
  const setTestResult = function(result) {
    testResult.value = result
    console.log('Test result saved:', result)
  }

  const clearTestResult = function() {
    testResult.value = null
    console.log('Test result cleared')
  }

  //유저 아이디를 넣으면 유저 정보를 주는 api
  const findNickname = async function(userId) {
    try {
      const response = await axios({
        method: 'get',
        url: `${API_URL}/accounts/users/${userId}/`,
      });
      console.log(response.data.nickname);
      return response.data.nickname;
    } catch (err) {
      console.error('Error fetching nickname:', err);
      return 'Unknown User';
    }
  }

  return { 
    tests, 
    API_URL, 
    getTests, 
    signUp, 
    logIn, 
    token, 
    logOut, 
    user, 
    updateProfile,
    testResult,  // 테스트 결과 상태 추가
    setTestResult,  // 테스트 결과 설정 함수
    clearTestResult,
    findNickname  
  }
}, {persist: true})