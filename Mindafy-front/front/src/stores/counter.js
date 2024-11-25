//counter.js
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
        Authorization: `Token ${token.value}`, // 인증 토큰 포함
      },
    })
      .then(() => {
        token.value = null; // 토큰 제거
        user.value = null
        router.push({ name: 'login' }); // 로그인 페이지로 이동
        console.log('로그아웃이 완료되었습니다.');
      })
      .catch(err => {
        console.error('로그아웃 요청 중 오류 발생:', err);
      });
  };



const updateProfile = async function (payload) {
  try {
    // 비밀번호가 있다면 password 변경 요청 (POST)
    if (payload.old_password && payload.new_password1 && payload.new_password2) {
      const passwordResponse = await axios({
        method: 'post',
        url: `${API_URL}/accounts/password/change/`,  // 비밀번호 변경 엔드포인트
        headers: {
          Authorization: `Token ${token.value}`,
        },
        data: {
          old_password: payload.old_password,  // 기존 비밀번호
          new_password1: payload.new_password1,  // 새 비밀번호
          new_password2: payload.new_password2,  // 새 비밀번호 확인
        },
      });
      console.log('Password updated:', passwordResponse.data);
    }

    // 닉네임이 있다면 nickname 변경 요청 (PATCH)
    if (payload.nickname) {
      const nicknameResponse = await axios({
        method: 'patch',
        url: `${API_URL}/accounts/users/${user.value.id}/nickname/`,  // 사용자 ID로 닉네임 변경
        headers: {
          Authorization: `Token ${token.value}`,
        },
        data: { nickname: payload.nickname },
      });
      console.log('Nickname updated:', nicknameResponse.data);
    }

    // 프로필 이미지가 있다면 profile_img 변경 요청 (PATCH)
    if (payload.profile_img) {
      const profileImgResponse = await axios({
        method: 'patch',
        url: `${API_URL}/accounts/users/${user.value.id}/profile_img/`,  // 사용자 ID로 프로필 이미지 변경
        headers: {
          Authorization: `Token ${token.value}`,
        },
        data: { profile_img: payload.profile_img },
      });
      console.log('Profile image updated:', profileImgResponse.data);
    }

    // 로컬 사용자 데이터 업데이트
    user.value = { ...user.value, ...payload };
    console.log('Profile updated:', user.value);
  } catch (err) {
    console.error('Error updating profile:', err); // 에러가 발생하면 자세한 로그 확인
    alert('Failed to update profile.'); // 오류 메시지
    throw err; // 에러를 다시 던져서 상위 레벨에서 처리할 수 있도록 함
  }


};
  

  return { tests, API_URL, getTests, signUp, logIn, token, logOut, user, updateProfile }
}, {persist: true})

