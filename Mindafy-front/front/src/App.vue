<template>
  <div id="app">
    <h1 @click="onClick">{{ title }}</h1>
    <RouterView/>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const title = ref('Mindafy');
const router = useRouter()
const onClick = function(){
  router.push({name:'test'})
}
</script>

<style scoped>
#app {
    text-align: center;
    padding: 20px;
}

h1 {
    color: #1D63FF; /* Primary blue color for the title */
    font-size: 2.5em;
    margin-bottom: 20px;
}
</style>