<!-- CommentListItem.vue -->
<template>
    <div>
      <p v-if="!isEditing">
        {{ nickname  }} - {{ comment.content }}
        <button v-if="isAuthor" @click="editComment">수정</button>
        <button v-if="isAuthor" @click="deleteComment">삭제</button>
      </p>

      <div v-else>
        <textarea v-model="editContent" rows="4"></textarea>
        <button @click="saveEdit">저장</button>
        <button @click="cancelEdit">취소</button>
      </div>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';

const props = defineProps({
  comment: Object,
});
const emit = defineEmits(['refreshComments'])
const store = useCounterStore();

//닉네임 표시 
const nickname = ref('Loading...');

onMounted(async () => {
  // console.log(await store.findNickname(props.comment.user));
  
  nickname.value = await store.findNickname(props.comment.user);
});
// 수정 관련 상태 변수
const isEditing = ref(false);  // 수정 모드 여부
const editContent = ref(props.comment.content);  // 수정할 내용

// 현재 유저가 댓글 작성자인지 확인
const isAuthor = computed(() => {
  return store.user?.id && props.comment?.user && store.user.id === props.comment.user;
});


// 수정 버튼 클릭 시 수정 모드로 전환
const editComment = () => {
  isEditing.value = true;
};

// 수정 취소
const cancelEdit = () => {
  isEditing.value = false;
  editContent.value = props.comment.content; // 원래 내용으로 되돌리기
};

// 댓글 수정 저장
const saveEdit = () => {
  if (editContent.value.trim() === '') {
    alert('댓글을 입력해주세요.');
    return;
  }

  axios({
    method: 'patch',
    url: `${store.API_URL}/api/v1/tests/${props.comment.test}/comments/${props.comment.id}/`,
    headers: {
      Authorization: `Token ${store.token}`, // 토큰 값 사용
    },
    data: {
      content: editContent.value, // 수정된 댓글 내용
    },
  })
    .then((res) => {
      console.log('댓글이 수정되었습니다.');
      props.comment.content = editContent.value;  // UI 업데이트
      isEditing.value = false;  // 수정 모드 종료
      emit('refreshComments'); // 댓글 목록 새로고침
    })
    .catch((error) => {
      console.error('댓글 수정 실패:', error);
      alert('댓글 수정에 실패했습니다. 다시 시도해주세요.');
    });
};


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
.comment-item {
    margin-bottom: 15px;
    padding-bottom: 10px;
    border-bottom: 1px solid #eaeaea; /* Light grey border */
}

button {
    background-color: transparent; /* Transparent background for edit/delete buttons */
    color: #1D63FF; /* Primary blue for buttons */
    border: none;
    cursor: pointer;
}

button:hover {
    text-decoration: underline; /* Underline on hover for clarity */
}

textarea {
    width: calc(100% - 20px);
    margin-top: 10px;
}
</style>