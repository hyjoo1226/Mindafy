<template>
<div>
    <h3>TestList</h3>
    <TestListItem v-for="test in store.tests" :key="test.id" :test="test"/>
</div>
</template>

<script setup>
import TestListItem from './TestListItem.vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()

</script>

<style scoped>

</style>