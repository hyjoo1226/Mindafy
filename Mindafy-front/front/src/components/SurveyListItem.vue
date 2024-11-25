<!-- SurveyListItem.vue -->
<template>
    <div v-for="surveyQ in surveyQs">
        <h4>
            {{ surveyQ.question }}
        </h4>
        <SurveyListItemOp :surveyQ="surveyQ" :survey="survey"/>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import { useRoute } from 'vue-router';
import SurveyListItemOp from './SurveyListItemOp.vue';

const route = useRoute()
const store = useCounterStore()
const surveyQs = ref(null)
const props = defineProps({
    survey:Object
})
const Qoptions = ref(null)
// console.log(props.survey.id);

onMounted(()=>{
    //surveyQ 정보 받아오기
    axios({
        method : 'get',
        url : `${store.API_URL}/api/v1/surveys/${props.survey.id}/questions/`
    })
        .then((res)=>{
            // console.log(res.data);
            surveyQs.value = res.data
            // surveys.value = res.data
        })
        .catch(err=>console.log(err))
})
</script>

<style scoped>

</style>