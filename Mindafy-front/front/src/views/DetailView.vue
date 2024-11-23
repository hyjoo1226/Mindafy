<!-- DetailView.vue -->
<template>
<div>
    <RouterLink :to="{name:'test'}">MainPage</RouterLink>
    <div v-if="test">
        <h1>{{ test.title }} 테스트 상세설명 페이지 입니다.</h1>
        <p>테스트 상세 설명 : {{ test.description }}</p>
        <button @click="onClick(test.id)">테스트 시작하기</button>
        <br>
        <hr>
        <br>
        <!-- 댓글 생성 폼 -->
        <div>
            <textarea v-model="newComment.content" placeholder="댓글을 작성해주세요..." rows="4"></textarea>
            <button @click="createComment">댓글 작성</button>
        </div>
        <!-- 댓글 목록 -->
        <CommentList ref="commentList" />
    </div>
</div>
</template>

<script setup>
import CommentList from '@/components/CommentList.vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

const store = useCounterStore()
const route = useRoute()
const test = ref(null)

const newComment = ref({
  content: '', // 댓글 내용
  parent_comment: null, // 부모 댓글 (기본은 null)
});
// 테스트 데이터를 가져오는 함수
onMounted(()=>{
    axios({
        method : 'get',
        url : `${store.API_URL}/api/v1/tests/${route.params.id}/`
    })
        .then((res)=>{
            test.value = res.data
        })
        .catch(err=>console.log(err))
})


// 댓글 생성 함수
const createComment = () => {
    if (newComment.value.content.trim() === '') {
        alert('댓글을 입력해주세요.');
        return;
    }

    // 댓글 생성 요청
    axios({
        method: 'post',
        url: `${store.API_URL}/api/v1/tests/${route.params.id}/comments/`,
        headers: {
            Authorization: `Token ${store.token}`, // 인증 토큰 헤더
        },
        data: {
            content: newComment.value.content,
            parent_comment: newComment.value.parent_comment,
        },
    })
        .then((res) => {
            console.log('댓글이 성공적으로 생성되었습니다.', res.data);
            newComment.value.content = ''; // 댓글 작성 후 입력창 초기화
            // 댓글 목록을 다시 불러오기 위해 댓글 리스트를 업데이트
            // 이 부분은 CommentList 컴포넌트에서 데이터를 재조회하도록 할 수 있습니다.
            // 예: CommentList.vue에서 댓글을 다시 가져오는 로직 추가
            refreshComments();
        })
        .catch((err) => {
            console.error('댓글 작성 실패:', err);
            alert('댓글 작성에 실패했습니다. 다시 시도해주세요.');
        });
};

// 댓글 목록 새로고침 함수
const commentList = ref(null);
const refreshComments = () => {
    commentList.value?.fetchComments(); // fetchComments 메서드 호출
}

</script>


<style scoped>

</style>