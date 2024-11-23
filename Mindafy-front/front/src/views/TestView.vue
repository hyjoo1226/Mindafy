<!-- TestView.vue -->
<template>
<div>
    <nav>
        <RouterLink :to="{name:'user'}">MyPage</RouterLink>
        <span> | </span>
        <RouterLink :to="{name:'signup'}">SignUp</RouterLink>
        <span> | </span>
        <RouterLink :to="{name:'login'}">LogIn</RouterLink>
        <LogOut/>
    </nav>
    <h1>TestPage</h1>
    <TestList/>
</div>
</template>

<script setup>
import LogOut from '@/components/LogOut.vue';
import TestList from '@/components/TestList.vue';
import { useCounterStore } from '@/stores/counter';
import { onMounted } from 'vue'
const store = useCounterStore()
onMounted(()=>{
    store.getTests()
})
</script>

<style scoped>

</style>