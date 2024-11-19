<!-- MainPageView.vue -->
<template>
    <div>
        <header>
            <img class="logo" src="@/assets/mindafyLogo.png" alt="Mindafy로고">
            <img class="icon search" src="@/assets/searchButton.png" alt="돋보기 이미지" @click="store.onSearchPage">
            <img class="icon user" src="@/assets/user.png" alt="User Basic 이미지" @click="store.onUserPage">
        </header>
        <h1 class="mindafy">Mindafy</h1>
        <div>
            <button class="button" @click="store.onTestListPage">테스트 시작하기</button>
        </div>
    </div>
</template>

<script setup>
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
.mindafy{
    position: absolute;
    width: 789px;
    height: 157px;
    left: calc(50% - 789px/2);
    top: 500px;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 700;
    font-size: 200px;
    line-height: 157px;
    color: #A1D6B2;
    text-shadow: 10px 10px 10px rgba(0, 0, 0, 0.25);
    -webkit-text-stroke: 2px black; /* 테두리 두께 2px, 색상은 검정 */
}
.button{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding: 20px;
    gap: 10px;

    position: absolute;
    width: 460px;
    height: 100px;
    left: calc(50% - 460px/2 - 0.5px);
    top: 1200px;

    background: #E8B86D;
    border-radius: 30px;
    font-size: 50px;
    font-weight: bolder;
}

/* 버튼을 감싸는 컨테이너에 flexbox 적용 */
.button-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding: 20px;
    gap: 10px;

    position: absolute;
    width: 460px;
    height: 100px;
    left: calc(50% - 460px/2 - 0.5px);
    top: 1200px;

    background: #E8B86D;
    border: 2px solid #000000;
    border-radius: 30px;
}
.logo{
    left: 50px;
    height: 100px; /* 이미지 크기 동일하게 설정 */
    width: 100px;
    position: absolute;
    top: 40px; /* 상단에서 20px 떨어지도록 설정 */
}


</style>