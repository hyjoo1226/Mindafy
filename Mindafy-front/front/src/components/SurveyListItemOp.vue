<!-- SurveyListItemOp.vue -->
<template>
    <div v-for="option in options">
        -{{option.option_text}}
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';

const options = ref(null)
const store = useCounterStore()
const props = defineProps({
    survey:Object,
    surveyQ:Object
})

onMounted(()=>{
    //surveyQop 정보 받아오기
    axios({
        method : 'get',
        url : `${store.API_URL}/api/v1/surveys/${props.survey.id}/questions/${props.surveyQ.id}/options/`
    })
        .then((res)=>{
            console.log(res.data);
            options.value = res.data
        })
        .catch(err=>console.log(err))

})
</script>

<style scoped>

</style>