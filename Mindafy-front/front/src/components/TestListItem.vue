<template>
<div>
    <h5 @click="onClick(test.title)">테스트 제목 : {{ test.title }}</h5>
    <!-- {{ test.content }} 이부분이 어떻게 정보를 불러와야할지 모르겠어 -->
    <p>테스트 설명 : {{ test.content }}</p>

</div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const props = defineProps({
    test:Object
})
const route = useRouter()
const onClick = function(testname){
    route.push({name:'detail', params:{testname:testname}})
}
</script>

<style scoped>

</style>