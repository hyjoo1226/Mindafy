<!-- StartView.vue -->
<template>
    <div class="start-page">
      <h1>{{ pageTitle }}</h1>
      <RouterLink :to="{name:'test'}" class="start-button">START</RouterLink>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const pageTitle = ref('Welcome to the Survey');
</script>

<style scoped>
.start-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

.start-button {
    background-color: #7ebc59; /* Accent green color for button */
    color: #FFFFFF;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    font-size: 1.2em;
}
</style>