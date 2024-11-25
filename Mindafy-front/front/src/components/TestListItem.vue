<!-- TestListItem.vue -->
<template>
    <div class="test-item">
      <h5 @click="onClick(test.id)" class="test-title">{{ test.title }}</h5>
      <p class="test-description">{{ test.description }}</p>
      <p class="test-recommendation">❤️ {{ test.recommendation_count }}</p>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const props = defineProps({
    test: Object
})

const router = useRouter()
const onClick = function(id){
    router.push({name:'detail', params:{id:id}})
}
</script>

<style scoped>
.test-item {
    padding: 10px;
    border-radius: 10px;
    border: 1px solid #eaeaea;
    margin-bottom: 10px;
    background-color: #ffffff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.test-title {
    cursor: pointer;
    color: #1D63FF;
    margin-bottom: 5px;
}

.test-description,
.test-recommendation {
    color: #666666;
}
</style>