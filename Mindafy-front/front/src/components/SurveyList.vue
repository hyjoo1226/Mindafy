<template>
    <div v-for="survey in surveys">
        <h2>
            {{ survey.title }}
        </h2>
        <SurveyListItem :survey="survey"/>
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

</script>

<style scoped>

</style>