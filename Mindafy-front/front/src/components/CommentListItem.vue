<!-- CommentListItem.vue -->
<template>
    <div>
      <p> - {{ comment.content }}
      <!-- <small>작성자 ID: {{ comment.user }}</small>
      <p>{{ store.user.id }}</p> -->
      <!-- 작성자만 삭제 버튼 표시 -->
        <button v-if="isAuthor" @click="deleteComment">삭제</button>
      </p>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref, computed } from 'vue';
import axios from 'axios';

const props = defineProps({
  comment: Object,
});
const store = useCounterStore();
const emit = defineEmits(['refreshComments'])



// 현재 유저가 댓글 작성자인지 확인
const isAuthor = computed(() => {
  return store.user?.id && props.comment?.user && store.user.id === props.comment.user;
});


// 댓글 삭제 함수
const deleteComment = () => {
  if (!confirm('정말로 댓글을 삭제하시겠습니까?')) return;
  axios({
    method: 'delete',
    url: `${store.API_URL}/api/v1/tests/${props.comment.test}/comments/${props.comment.id}/`, // 댓글 ID 포함
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(() => {
      console.log('댓글이 삭제되었습니다.');
      emit('refreshComments'); // 댓글 목록 새로고침
    })
    .catch((error) => {
      console.error('댓글 삭제 실패:', error);
    });
};
</script>

<style scoped>

</style>