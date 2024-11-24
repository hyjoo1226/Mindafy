<!-- TestListItem.vue -->
<template>
<div>
    <h5 @click="onClick(test.id)">테스트 제목 : {{ test.title }}</h5>
    <p>테스트 설명 : {{ test.description }}</p>
    <p>❤️ : {{ test.recommendation_count }}</p>
    <hr>

</div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const props = defineProps({
    test:Object
})

const route = useRouter()
const onClick = function(id){
    route.push({name:'detail',params:{id:id}})

}
</script>

<style scoped>

</style>