<!-- CommentList.vue -->
<template>
    <div>
        <h3>댓글</h3>
        <div v-if="comments.length > 0">
            <CommentListItem 
                v-for="comment in comments" 
                :key="comment.id" 
                :comment="comment" />
        </div>
        <div v-else>
            <p>아직 댓글이 없습니다. 첫 번째 댓글을 남겨보세요!</p>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';
import { useRoute } from 'vue-router';
import CommentListItem from './CommentListItem.vue';

const store = useCounterStore();
const route = useRoute();
const comments = ref([]);

// 테스트의 댓글을 가져오는 함수
const fetchComments = () => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/tests/${route.params.id}/comments/`,
    })
        .then((res) => {
        comments.value = res.data;
        })
        .catch((err) => console.log(err));
};

// 컴포넌트가 마운트되면 댓글을 가져옵니다.
onMounted(() => {
    fetchComments();
});
</script>

<style scoped>
</style>