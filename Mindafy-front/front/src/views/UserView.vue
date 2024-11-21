<!-- UserView.vue -->
<template>
<div>
    <RouterLink :to="{name:'test'}">MainPage</RouterLink>
    <LogOut/>
    <h1>My Profile Page</h1>
    <form @submit.prevent="updateProfile">
    <label for="nickname">Nickname : </label>
    <input type="text" id="nickname" v-model="nickname" />
    <br>

    <!-- <label for="password">New Password : </label>
    <input type="password" id="password" v-model="password" />
    <br> -->
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
    <p>Email : {{ store.user.email }}</p>
    <p>Age : {{ store.user.age }}</p>
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
        // }), // 비밀번호 관련 값이 있으면 포함
    };

    try {
        // 프로필 업데이트
        await store.updateProfile(payload);
        alert('Profile updated successfully!');
    } catch (error) {
        alert('Failed to update profile.');
    }
};
</script>

<style scoped>
/* 스타일 작성 */
</style>
  