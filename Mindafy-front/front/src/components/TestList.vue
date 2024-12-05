<!-- TestList.vue -->
<template>
    <div class="test-list">
      <!-- <h3>TestList</h3> -->
      <div class="test-items-container">
          <TestListItem v-for="test in store.tests" :key="test.id" :test="test"/>
      </div>
    </div>
</template>

<script setup>
import TestListItem from './TestListItem.vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
</script>

<style scoped>
.test-list {
    margin-top: 20px;
}

.test-items-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
}

@media (max-width: 768px) {
    .test-items-container {
        grid-template-columns: 1fr;
    }
}
</style>