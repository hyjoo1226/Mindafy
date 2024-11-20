<template>
<div>
    <RouterLink :to="{name:'test'}">MainPage</RouterLink>
    <h1>{{ test.title }} 테스트 상세설명 페이지 입니다.</h1>
    <p>테스트 상세 설명 : {{ test.description }}</p>
    <button @click="onClick(test.id)">테스트 시작하기</button>
</div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';


const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const testId = ref(route.params.testId) //여기에 testId가 저장돼 있다. 이걸로 store에서 해당 객체의 정보를 가져온다.
const test = ref(store.TestIdToTest(testId.value))

const onClick = function(testId){
    router.push({name:'survey',params:{testId}})
}
</script>


<style scoped>

</style>