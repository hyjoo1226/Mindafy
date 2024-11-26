<!-- TestListItem.vue -->
<template>
    <div class="test-item">
      <div class="test-item-image">
          <img :src="`http://127.0.0.1:8000/static/${test.test_img}`" :alt="test.title">
      </div>
      <div class="test-item-content">
        <h5 @click="onClick(test.id)" class="test-title">{{ test.title }}</h5>
        <p class="test-description">{{ test.description }}</p>
        <p class="test-recommendation">❤️ {{ test.recommendation_count }}</p>
      </div>
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
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
    position: relative;
}

.test-item-image {
    width: 70%;
    height: 50%;
    flex-shrink: 0;
}

.test-item-image img {
  width: 100%; 
  height: 100%; 
  object-fit: cover;
  border-radius: 8px;
}

.test-item-content {
    display: flex;
    flex-direction: column;
    width: 100%;
    min-height: 150px;
    padding-bottom: 30px;
}

.test-title {
    cursor: pointer;
    color: #1D63FF;
    font-size: 17px;
    margin-bottom: 5px;
}

.test-description {
    color: #666666;
    font-size: 14px;
    flex-grow: 1;
}

.test-recommendation {
    color: #666666;
    font-size: 15px;
    position: absolute;
    bottom: 0;
    right: 10px;
    display: flex;
    align-items: center;
    gap: 4px;
}


</style>