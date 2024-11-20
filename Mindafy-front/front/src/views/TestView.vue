<template>
<div>
    <RouterLink :to="{name:'user'}">MyPage</RouterLink>
    <h1>TestPage</h1>
    <TestList/>
</div>
</template>

<script setup>
import TestList from '@/components/TestList.vue';


</script>

<style scoped>

</style>