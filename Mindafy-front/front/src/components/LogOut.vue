<!-- LogOut.vue -->
<template>
    <div>
      <button @click="logOut" v-show="store.token">Log Out</button>
    </div>
  </template>
  
  <script setup>
  import { useCounterStore } from '@/stores/counter';
  
  const store = useCounterStore();
  
  const logOut = () => {
    store.logOut()
  };
  </script>
  
  <style scoped>
  
  </style>
  