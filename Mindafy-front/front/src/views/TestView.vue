<template>
<div>
    <h1>TestPage</h1>
    <RouterLink :to="{name:'user'}">MyPage</RouterLink>
    <TestList/>
</div>
</template>

<script setup>
import TestList from '@/components/TestList.vue';


</script>

<style scoped>

</style>