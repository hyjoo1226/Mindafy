<template>
<div>
    <RouterLink :to="{name:'test'}">MainPage</RouterLink>
    <h1>SignUp Page</h1>
    <form @submit.prevent="signUp">
        <label for="usrname">id : </label>
        <input type="text" id="usrname" v-model.trim="username"><br>

        <label for="password1">password : </label>
        <input type="password" id="password1" v-model.trim="password1"><br>

        <label for="password2">password confirmation : </label>
        <input type="password" id="password2" v-model.trim="password2"><br>

        <label for="nickname">nick name : </label>
        <input type="text" id="nickname" v-model.trim="nickname"><br>

        <label for="age">age : </label>
        <input type="number" id="age" v-model.trim="age"><br>

        <label for="email">email : </label>
        <input type="email" id="email" v-model.trim="email"><br>

        <label for="profile_img">profile img : </label>
        <input type="text" id="profile_img" v-model.trim="profile_img"><br>

        <input type="submit" value="SignUp">
    </form>
</div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue';

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const age = ref(null)
const email = ref(null)
const profile_img = ref(null)

const store = useCounterStore()
const signUp = function(){
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      nickname: nickname.value,
      age: age.value,
      email: email.value,
      profile_img: profile_img.value
    }
    store.signUp(payload)
}
</script>

<style scoped>

</style>