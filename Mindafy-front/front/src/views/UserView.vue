<template>
<div>
    <RouterLink :to="{name:'test'}">MainPage</RouterLink>
    <LogOut/>
    <h1>UserPage</h1>
    <p>id : {{ store.user.username }}</p>
    <p>nickname : {{ store.user.nickname }}</p>
    <p>email : {{ store.user.email }}</p>
    <p>age : {{ store.user.age }}</p>
    <p>profile_img : {{ store.user.profile_img }}</p>
</div>
</template>

<script setup>

import LogOut from '@/components/LogOut.vue';
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()

</script>

<style scoped>

</style>