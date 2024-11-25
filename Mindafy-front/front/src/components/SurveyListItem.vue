<!-- SurveyListItem.vue -->
<template>
    <div class="survey-questions">
      <!-- 7점 척도 안내문을 문항 리스트 상단에 배치 -->
      <div v-if="hasScaleQuestions" class="scale-guide mb-4">
        <p>나에게 알맞는 항목을 선택해주세요.</p>
      </div>
      
      <div v-for="surveyQ in surveyQs" :key="surveyQ.id" class="survey-question">
        <h4>{{ surveyQ.question }}</h4>
        <SurveyListItemOp 
          :surveyQ="surveyQ" 
          :survey="survey"
          @answer-selected="handleAnswer"
        />
      </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import { useRoute } from 'vue-router';
import SurveyListItemOp from './SurveyListItemOp.vue';

const route = useRoute();
const store = useCounterStore();
const surveyQs = ref(null);

const props = defineProps({
    survey: Object
});

// 7점 척도 문항이 있는지 확인
const hasScaleQuestions = computed(() => {
    return surveyQs.value?.some(q => !q.hasOptions);
});

const emits = defineEmits(['update-answers']);

const handleAnswer = (answerData) => {
    console.log('Received answer from SurveyListItemOp:', answerData);
    emits('update-answers', answerData); // 상위 컴포넌트로 전달
};

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/surveys/${props.survey.id}/questions/`
    })
        .then((res) => {
            surveyQs.value = res.data;
        })
        .catch(err => console.log(err));
});
</script>

<style scoped>
.survey-questions {
margin: 1rem 0;
}

.scale-guide {
background-color: #f3f4f6;
padding: 1rem;
border-radius: 0.5rem;
margin-bottom: 1.5rem;
}

.survey-question {
margin-bottom: 1.5rem;
}
</style>