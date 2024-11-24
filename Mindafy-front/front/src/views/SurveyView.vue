<!-- Survet.View.vue -->
<template>
<div v-if="test">
    <RouterLink :to="{name:'test'}">MainPage</RouterLink>
    <h1>{{test.title}} <br>설문조사 페이지입니다.</h1>
    <SurveyList :testId="test.id"/>
</div>
</template>

<script setup>
import { ref,onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';
import SurveyList from '@/components/SurveyList.vue';


const route = useRoute()
const store = useCounterStore()
const test = ref(null)
// const surveys = ref(null)

onMounted(()=>{
    //test 정보 받아오기
    axios({
        method : 'get',
        url : `${store.API_URL}/api/v1/tests/${route.params.id}/`
    })
        .then((res)=>{
            test.value = res.data
            // console.log(res.data);
            
        })
        .catch(err=>console.log(err))

    // //survey 정보 받아오기
    // axios({
    //     method : 'get',
    //     url : `${store.API_URL}/api/v1/tests/${route.params.id}/surveys`
    // })
    //     .then((res)=>{
    //         console.log(res.data);
    //         surveys.value = res.data
    //     })
    //     .catch(err=>console.log(err))
})
</script>

<style scoped>

</style>