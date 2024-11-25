<!-- LogInView.vue -->
<template>
<div>
    <!-- <RouterLink :to="{name:'test'}">MainPage</RouterLink> -->
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
div {
    max-width: 400px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
    color: #333333;
}

form {
    display: flex;
    flex-direction: column;
}

label {
    margin-bottom: 5px;
    font-weight: bold;
}

input[type="text"],
input[type="password"] {
    margin-bottom: 15px;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ddd;
}

input[type="submit"] {
    background-color: #7ebc59; /* Accent green color */
    color: #FFFFFF;
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #6aa84f; /* Slightly darker green for hover */
}
</style>