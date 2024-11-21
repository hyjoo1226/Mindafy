<template>
<div>
    <RouterLink :to="{name:'test'}">MainPage</RouterLink>
    <h1>LogIn View</h1>
    <form @submit.prevent="logIn">
        <label for="username">id : </label>
        <input type="text" id="username" v-model.trim="username"><br>

        <label for="password">password : </label>
        <input type="password" id="password" v-model.trim="password"><br>

        <input type="submit" value="logIn">
    </form>
</div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue';

const username = ref(null)
const password = ref(null)

const store = useCounterStore()

const logIn = function(){
    const payload = {
        username: username.value,
        password: password.value
    }
    store.logIn(payload)
}
</script>

<style scoped>

</style>