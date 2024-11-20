<template>
<div>
    <h1>LogIn View</h1>
    <form>
        <label for="username">username : </label>
        <input type="text" id="username" v-model.trim="username"><br>

        <label for="password">password : </label>
        <input type="text" id="password" v-model.trim="password"><br>

        <input type="submit" value="logIn">
    </form>
</div>
</template>

<script setup>
import { ref } from 'vue';

const username = ref(null)
const password = ref(null)
</script>

<style scoped>

</style>