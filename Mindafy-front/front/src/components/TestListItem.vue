<template>
<div>
    <h5 @click="onClick(test.id)">테스트 제목 : {{ test.title }}</h5>
    <p>테스트 설명 : {{ test.description }}</p>

</div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const props = defineProps({
    test:Object
})
const route = useRouter()
const onClick = function(testId){
    route.push({name:'detail',params:{testId}})

}
</script>

<style scoped>

</style>