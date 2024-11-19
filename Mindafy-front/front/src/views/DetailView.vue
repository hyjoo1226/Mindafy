<template>
<div>
    <h1>{{testName}} 테스트 상세설명 페이지 입니다.</h1>
    <p>테스트 상세 설명 : {{ testContent }}</p>
    <button @click="onClick">테스트 시작하기</button>
</div>
</template>

<script setup>
import { computed, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter()
const testName = ref(route.params.testname)

const onClick = function(){
    router.push({name:'survey'})
}
</script>


<style scoped>

</style>