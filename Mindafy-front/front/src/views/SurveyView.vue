<template>
    <div v-if="test">
      <h1>{{ test.title }}의 설문조사 페이지입니다.</h1>
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
import { ref, onMounted } from 'vue';
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
    .then((res) => {
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
        console.log('제출할 답변들:', answers.value);
        
        const response = await axios({
            method: 'post',
            url: `${store.API_URL}/api/v1/tests/results/${theResult.value.id}/surveys/answers/`,
            data: { answers: answers.value }
        });

        console.log('모든 답변이 성공적으로 제출되었습니다.');
        
        // 답변 제출 성공 후 알고리즘 계산 요청
        const calculateResponse = await axios({
            method: 'post',
            url: `${store.API_URL}/api/v1/tests/results/${theResult.value.id}/calculate/`
        });
        
        console.log('알고리즘 함수 작동 성공.');
        console.log(`이것은 알고리즘 작동 성공 후 resData입니다. : ${JSON.stringify(calculateResponse.data)}`);

        // Pinia store에 결과 저장
        store.setTestResult(calculateResponse.data);

        // 결과 페이지로 이동
        router.push({ 
            name: 'result',
        });
    } catch (err) {
        console.error('오류 발생:', err);
        alert('처리 중 오류가 발생했습니다.');
    }
};
</script>

<style scoped>
div {
    padding: 20px;
}

h1 {
    margin-bottom: 20px;
    color: #333333;
}

button {
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #1D63FF;
    color: #FFFFFF;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #155ab3;
}
</style>