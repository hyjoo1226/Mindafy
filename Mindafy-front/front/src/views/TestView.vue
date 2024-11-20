<template>
<div>
    <nav>
        <RouterLink :to="{name:'user'}">MyPage</RouterLink>
        <span> | </span>
        <RouterLink :to="{name:'signup'}">SignUp</RouterLink>
        <span> | </span>
        <RouterLink :to="{name:'login'}">LogIn</RouterLink>
    </nav>
    <h1>TestPage</h1>
    <TestList/>
</div>
</template>

<script setup>
import TestList from '@/components/TestList.vue';


</script>

<style scoped>

</style>