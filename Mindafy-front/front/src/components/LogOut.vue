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
button {
    background-color: #7ebc59; /* Accent green color */
    color: #FFFFFF;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #6aa84f; /* Slightly darker green for hover */
}
</style>
  