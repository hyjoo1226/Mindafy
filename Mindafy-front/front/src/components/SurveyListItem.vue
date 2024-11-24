<template>
    <div v-for="surveyQ in surveyQs">
        {{ surveyQ.question }}
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import { useRoute } from 'vue-router';
const route = useRoute()
const store = useCounterStore()
const surveyQs = ref(null)
const props = defineProps({
    survey:Object
})
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