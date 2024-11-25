<!-- Survey.View.vue -->
<template>
    <div v-if="test">
      <RouterLink :to="{ name: 'test' }">MainPage</RouterLink>
      <h1>{{ test.title }}의 <br>설문조사 페이지입니다.</h1>
      <SurveyList 
        :testId="test.id"
        @update-answers="updateAnswers"
      />
      <button 
        @click="submitSurvey"
        class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
      >
        제출하기
      </button>
    </div>
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

const answers = ref([]);

const updateAnswers = (answerData) => {
    console.log('Updating answers in SurveyView:', answerData);
    const existingAnswerIndex = answers.value.findIndex(
        a => a.question_id === answerData.question_id
    );
    if (existingAnswerIndex !== -1) {
        answers.value[existingAnswerIndex] = answerData;
    } else {
        answers.value.push(answerData);
    }
    console.log('Current answers:', answers.value);
};

const submitSurvey = async () => {
    try {
        // Submit each answer
        console.log(`answers.value : ${answers.value}`);
        
        for (const answer of answers.value) {
            console.log('Sending answer:', answers.value);
            await axios({
                method: 'post',
                url: `${store.API_URL}/api/v1/tests/results/${theResult.value.id}/surveys/answers/`,
                data: answer
            });
        }
        console.log('모든 답변이 제출되었습니다.');
        router.push({ name: 'result' });
    } catch (err) {
        console.error(err);
        alert('답변 제출에 실패하였습니다.');
    }
};

</script>

<style scoped>

</style>

