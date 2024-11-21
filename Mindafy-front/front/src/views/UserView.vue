<template>
<div>
    <RouterLink :to="{name:'test'}">MainPage</RouterLink>
    <h1>UserPage</h1>
    <p>{{ store.user.username }}</p>
    <p>{{ store.user.nickname }}</p>
    <p>{{ store.user.email }}</p>
    <p>{{ store.user.age }}</p>
    <p>{{ store.user.profile_img }}</p>
</div>
</template>

<script setup>

import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()

</script>

<style scoped>

</style>