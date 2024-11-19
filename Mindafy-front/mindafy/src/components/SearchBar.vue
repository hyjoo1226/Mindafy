<!-- SearchBar.vue -->
<template>
    <div>
        <form @submit.prevent="onSubmit">
            <input 
                type="text" 
                v-model="inputData" 
                placeholder="검색어를 입력하세요" 
            >
            <button type="submit" aria-label="검색">
                search
            </button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
// 부모 컴포넌트로부터 검색 이벤트 핸들러를 전달받기
const inputData = ref('');
const store = useCounterStore()
function onSubmit() {
    store.search(inputData.value);
    inputData.value = ''; // 검색 후 입력 필드 초기화
}
</script>

<style scoped>

</style>
