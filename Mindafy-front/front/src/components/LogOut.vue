<!-- LogOut.vue -->
<template>
    <div>
      <button @click="logOut">Log Out</button>
    </div>
  </template>
  
  <script setup>
  import { useCounterStore } from '@/stores/counter';
  
  const store = useCounterStore();
  
  const logOut = () => {
    store.logOut(); // Pinia의 logOut 메서드 호출
  };
  </script>
  
  <style scoped>
  /* 스타일 정의 */
  </style>
  