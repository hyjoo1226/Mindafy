<!-- SignUpView -->
<template>
<div>
    <!-- <h3 v-if="errorMessage" class="error">{{ store.signUp.errorMessage }}</h3> -->
    <!-- <RouterLink :to="{name:'test'}">MainPage</RouterLink> -->
    <!-- <h1>SignUp Page</h1> -->
    <form @submit.prevent="signUp">
        <label for="usrname">아이디</label>
        <input type="text" id="usrname" v-model.trim="username"><br>

        <label for="password1">비밀번호</label>
        <input type="password" id="password1" v-model.trim="password1"><br>

        <label for="password2">비밀번호 확인</label>
        <input type="password" id="password2" v-model.trim="password2"><br>

        <label for="nickname">닉네임</label>
        <input type="text" id="nickname" v-model.trim="nickname"><br>

        <label for="age">나이</label>
        <input type="number" id="age" v-model="age"><br>

        <label for="email">이메일</label>
        <input type="email" id="email" v-model.trim="email"><br>

        <!-- <label for="profile_img">프로필 사진</label>
        <input type="text" id="profile_img" v-model="profile_img"><br> -->

        <input type="submit" value="회원가입">
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
    text-align: left;
}

input[type="text"],
input[type="password"],
input[type="number"],
input[type="email"] {
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