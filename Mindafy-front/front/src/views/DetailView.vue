<!-- DetailView.vue -->
<template>
<div>
    <RouterLink :to="{name:'test'}">MainPage</RouterLink>
    <div v-if="test">
        <h1>{{ test.title }} 테스트 상세설명 페이지 입니다.</h1>
        <p>테스트 상세 설명 : {{ test.description }}</p>
        <button @click="onClick(test.id)">테스트 시작하기</button>

        <CommentList />
    </div>
</div>
</template>

<script setup>
import CommentList from '@/components/CommentList.vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

const store = useCounterStore()
const route = useRoute()
const test = ref(null)
onMounted(()=>{
    axios({
        method : 'get',
        url : `${store.API_URL}/api/v1/tests/${route.params.id}/`
    })
        .then((res)=>{
            test.value = res.data
        })
        .catch(err=>console.log(err))
})

// const onClick = function (id) {
//   route.push({ name: 'detail', params: { id: id } });
// };

</script>


<style scoped>

</style>