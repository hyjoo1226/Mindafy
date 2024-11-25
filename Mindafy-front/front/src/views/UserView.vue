<!-- UserView.vue -->
<template>
<div>
    <!-- <RouterLink :to="{name:'test'}">MainPage</RouterLink> -->
    <h1>My Profile Page</h1>
    <form @submit.prevent="updateProfile">
        <label for="nickname">Nickname : </label>
        <input type="text" id="nickname" v-model="nickname" />
        <br>
        
        <label for="old-password">Old Password : </label>
        <input type="password" id="old-password" v-model="oldPassword" />
        <br>
        
        <label for="new-password1">New Password : </label>
        <input type="password" id="new-password1" v-model="newPassword1" />
        <br>
        
        <label for="new-password2">Confirm New Password : </label>
        <input type="password" id="new-password2" v-model="newPassword2" />
        <br>
        
        <label for="profile-img">Profile Image : </label>
        <input type="text" id="profile-img" v-model="profileImg" />
        <br>
        
        <button type="submit">Save Changes</button>
    </form>
    <!-- <LogOut/> -->
    <!-- <p>Email : {{ store.user.email }}</p>
    <p>Age : {{ store.user.age }}</p> -->
</div>
</template>

<script setup>
import LogOut from '@/components/LogOut.vue';
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue';

const store = useCounterStore();

const nickname = ref(store.user.nickname);
const profileImg = ref(store.user.profile_img);
const oldPassword = ref(''); // 기존 비밀번호
const newPassword1 = ref(''); // 새 비밀번호
const newPassword2 = ref(''); // 새 비밀번호 확인

const updateProfile = async () => {
// payload 준비
    const payload = {
        nickname: nickname.value,
        profile_img: profileImg.value,
        old_password: oldPassword.value,
        new_password1: newPassword1.value,
        new_password2: newPassword2.value,
    };

    try {
        // 프로필 업데이트
        await store.updateProfile(payload);
        alert('정보변경이 완료되었습니다.');
    } catch (error) {
        alert('ERROR');
    }
};
</script>

<style scoped>
div {
    max-width: 500px;
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

button[type="submit"] {
    background-color: #7ebc59; /* Accent green color */
    color: #FFFFFF;
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #6aa84f; /* Slightly darker green for hover */
}

p {
    margin-top: 10px;
    color: #666666; /* Medium grey for less prominent text */
}
</style>