<template>
<div>
    <h1>{{testTitle}} 설문조사 페이지입니다.</h1>
</div>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute()
const testTitle = ref(route.params.testname)
</script>

<style scoped>

</style>