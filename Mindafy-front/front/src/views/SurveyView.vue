<!-- Survey.View.vue -->
<template>
<div v-if="test">
    <RouterLink :to="{name:'test'}">MainPage</RouterLink>
    <h1>{{test.title}}의 <br>설문조사 페이지입니다.</h1>
    <SurveyList :testId="test.id"/>
</div>
<button @click="submitSurvey(payload)">제출하기</button>
</template>

<script setup>
import { ref,onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';
import SurveyList from '@/components/SurveyList.vue';
import router from '@/router';


const route = useRoute()
const store = useCounterStore()
const test = ref(null)
const surveys = ref(null)

const theResult = ref(null)
onMounted(()=>{
    //test 정보 받아오기
    axios({
        method : 'get',
        url : `${store.API_URL}/api/v1/tests/${route.params.id}/`
    })
        .then((res)=>{
            test.value = res.data
            console.log(res.data);
            
        })
        .catch(err=>console.log(err))

    //survey 정보 받아오기
    axios({
        method : 'get',
        url : `${store.API_URL}/api/v1/tests/${route.params.id}/surveys`
    })
        .then((res)=>{
            console.log(res.data);
            surveys.value = res.data
        })
        .catch(err=>console.log(err))

    // 테스트 시작 시 TheResult 객체 생성
    axios({
    method:'post',
    url:`${store.API_URL}/api/v1/tests/${route.params.id}/start/`,
    })
    .then(res => {
    console.log(`TheResult : ${res.data}. 객체생성에 성공하였습니다.`);
    theResult.value = res.data
    })
    .catch((err)=>{
    console.log(err)
    alert('테스트 시작 시 TheResult 객체 생성에 실패하였습니다.')
    })
})

const answer_value = ref()
const question_id = ref()
const payload = {
    answer_value:answer_value.value,
    question_id:question_id.value
}

const submitSurvey = function(payload){
  const answer_value = payload.answer_value
  const question_id = payload.question_id
    
  axios({
      method:'post',
      url:`${store.API_URL}/api/v1/tests/results/${theResult.value.id}/surveys/answers`,
      data: {
          answer_value, question_id
      }
  })
      .then(res => {
          console.log(res.data);
          console.log('답변제출이 완료 되었습니다.');
          router.push({name:'result'})
          
      })
      .catch((err) => {
          console.log(err)
          console.log('답변 제출에 실패하였습니다.');
          
      });
}

</script>

<style scoped>

</style>