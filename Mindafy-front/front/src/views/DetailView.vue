<!-- DetailView.vue -->
<template>
    <div class="detail-container">
      <!-- <RouterLink :to="{name:'test'}" class="nav-link">MainPage</RouterLink> -->
      <div v-if="test">
        <h1>{{ test.title }} 테스트 상세설명 페이지 입니다.</h1>
        <p>테스트 상세 설명 : {{ test.description }}</p>
        <p>❤️ : {{ test.recommendation_count }}</p>
        <button v-if="store.token && is_like !== null" @click="toggleLike" class="like-button">
          {{ is_like ? '❤️' : '🤍' }}
        </button>
        <br>
        <button @click="onClick(test.id)">테스트 시작하기</button>
        <hr>
        <div class="comment-form">
          <textarea v-model="newComment.content" placeholder="댓글을 작성해주세요..." rows="4"></textarea>
          <button @click="createComment">댓글 작성</button>
        </div>
        <CommentList ref="commentList" />
      </div>
    </div>
</template>

<script setup>
import CommentList from '@/components/CommentList.vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const test = ref(null)
const is_like = ref(null); // 좋아요 상태를 로컬에서 관리

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
            console.log(res.data);
            
        })
        .catch(err=>console.log(err))

    if (store.token) {
        axios({
            method: 'get',
            url: `${store.API_URL}/api/v1/tests/${route.params.id}/likes/test/`,
            headers: {
                Authorization: `Token ${store.token}`,
            },
        })
            .then((res) => {
                console.log('Like status response:', res.data.is_like); // API 응답 확인
                is_like.value = res.data.is_like
            })
            .catch((err) => console.error('Failed to fetch liked status:', err));
    }
})

// 좋아요 토글 기능
const toggleLike = () => {
    // 좋아요 추가
    axios({
        method: 'post',
        url: `${store.API_URL}/api/v1/tests/${route.params.id}/likes/test/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
        .then(() => {
            // 서버 요청 성공 시에만 is_like 상태 변경
            if (is_like.value) {
                test.value.recommendation_count--; // 좋아요 수 감소
                alert('좋아요 취소가 반영되었습니다.');
            } else {
                test.value.recommendation_count++; // 좋아요 수 증가
                alert('좋아요가 반영되었습니다.');
            }
            is_like.value = !is_like.value; // 상태 변경
        })
        .catch(err => {
            console.error(err);
            alert('좋아요 요청에 실패했습니다.');
        });
};


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
            alert('로그인이 필요한 서비스입니다.');
        });
};

// 댓글 목록 새로고침 함수
const commentList = ref(null);
const refreshComments = () => {
    commentList.value?.fetchComments(); // fetchComments 메서드 호출
}

const onClick = function(id){
    router.push({name:'survey',params:{id:id}})
}

</script>


<style scoped>
.detail-container {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h1 {
    color: #333333;
}

p {
    color: #666666;
}

.like-button, button {
    margin-top: 10px;
}

textarea {
    width: 100%;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ddd;
}

.like-button:hover, button:hover {
    background-color: #6aa84f; /* Slightly darker green for hover */
}
</style>