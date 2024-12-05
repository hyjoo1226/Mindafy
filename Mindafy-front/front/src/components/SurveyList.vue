<!-- SurveyList.vue -->
<template>
    <div v-for="survey in surveys">
        <!-- <h2>
            {{ survey.title }}
        </h2> -->
        <SurveyListItem :survey="survey" @update-answers="updateAnswers"/>
    </div>
</template>

<script setup>
import SurveyListItem from './SurveyListItem.vue';
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import { useRoute } from 'vue-router';
const route = useRoute()
const store = useCounterStore()
const surveys = ref(null)
const props = defineProps({
    testId:Number
})
// emits 정의 추가
const emit = defineEmits(['update-answers']);

onMounted(()=>{
    //survey 정보 받아오기
    axios({
        method : 'get',
        url : `${store.API_URL}/api/v1/tests/${props.testId}/surveys`
    })
        .then((res)=>{
            console.log(res.data);
            surveys.value = res.data
        })
        .catch(err=>console.log(err))
})

// updateAnswers 함수 추가
const updateAnswers = (answerData) => {
    console.log('Received answer from SurveyListItem:', answerData);
    emit('update-answers', answerData); // SurveyView로 전달
};
</script>

<style scoped>
div {
    margin-bottom: 20px;
}

h2 {
    margin-bottom: 10px;
    color: #333333;
}
</style>