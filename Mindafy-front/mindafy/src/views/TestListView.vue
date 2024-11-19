<!-- TestListView.vue -->
<template>
    <div>
        <header>
            <img class="logo" src="@/assets/mindafyLogo.png" alt="Mindafy로고">
            <img class="icon search" src="@/assets/searchButton.png" alt="돋보기 이미지" @click="store.onSearchPage">
            <img class="icon user" src="@/assets/user.png" alt="User Basic 이미지" @click="store.onUserPage">
            <h1 @click="store.onTestListPage">Mindafy</h1>
        </header>
        <div>
            <TestListCarousel/>
        </div>
    </div>
</template>

<script setup>
import TestListCarousel from '@/components/TestListCarousel.vue';
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()
</script>

<style scoped>
.icon {
  height: 80px; /* 이미지 크기 동일하게 설정 */
  width: 80px;
  position: absolute;
  top: 60px; /* 상단에서 20px 떨어지도록 설정 */
}

/* 돋보기 이미지 오른쪽으로 배치 */
.search {
  right: 140px; /* 우측에서 80px 떨어지도록 설정 */
}

/* 사용자 이미지 우측에 배치 */
.user {
  right: 50px; /* 우측에서 20px 떨어지도록 설정 */
}
.logo{
    left: 50px;
    height: 100px; /* 이미지 크기 동일하게 설정 */
    width: 100px;
    position: absolute;
    top: 40px; /* 상단에서 20px 떨어지도록 설정 */
}
</style>