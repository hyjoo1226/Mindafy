<!-- SurveyListItemOp.vue -->
<template>
    <div class="question-options">
        <!-- Multiple choice options -->
        <div v-if="options && options.length > 0" class="multiple-choice">
            <div v-for="(option, index) in options" :key="option.id" class="option-item">
                <label class="flex items-center space-x-2">
                    <input 
                        type="radio" 
                        :name="'question-' + props.surveyQ.id"
                        :value="index + 1"
                        v-model="selectedAnswer"
                        @change="emitAnswer"
                        class="form-radio"
                    >
                    <span>{{ option.option_text }}</span>
                </label>
            </div>
        </div>

        <!-- 7-point scale -->
        <div v-else class="scale-rating">
            <div class="option-item">
                <p class="option-text"></p> 
                <!-- p에 써넣으면 됨. 질문에 대한 평가를 선택해주세요: -->
                <div class="scale-container">
                    <div v-for="n in 7" :key="n" class="scale-item">
                        <input 
                            type="radio" 
                            :id="`question-${props.surveyQ.id}-scale-${n}`"
                            :name="'question-' + props.surveyQ.id"
                            :value="n"
                            v-model="scaleValue"
                            @change="emitAnswer"
                        />
                        <label :for="`question-${props.surveyQ.id}-scale-${n}`">{{ n }}</label>
                    </div>
                </div>
                <div class="scale-labels">
                    <span>전혀 그렇지 않다</span>
                    <span>매우 그렇다</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';

const options = ref(null);
const store = useCounterStore();
const selectedAnswer = ref(null);
const scaleValue = ref(null);

const props = defineProps({
    survey: Object,
    surveyQ: Object
});

const emits = defineEmits(['answer-selected']);

const emitAnswer = () => {
    console.log('Emitting answer:', {
        question_id: props.surveyQ.id,
        answer_value: options.value?.length > 0 ? selectedAnswer.value : scaleValue.value
    });
    const answerPayload = {
        question_id: props.surveyQ.id,
        answer_value: options.value?.length > 0 ? selectedAnswer.value : scaleValue.value
    };
    console.log('Emitting answer:', answerPayload);
    emits('answer-selected', answerPayload);
};


onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/surveys/${props.survey.id}/questions/${props.surveyQ.id}/options/`
    })
        .then((res) => {
            options.value = res.data;
        })
        .catch(err => console.log(err));
});
</script>

<style scoped>
.question-options {
    margin: 20px 0;
}

.option-item {
    margin-bottom: 20px;
    padding: 15px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
}

.option-text {
    margin-bottom: 10px;
    font-size: 16px;
}

.scale-container {
    display: flex;
    justify-content: space-between;
    margin: 10px 0;
    padding: 0 20px;
}

.scale-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
}

.scale-item input[type="radio"] {
    width: 30px;
    height: 30px;
    cursor: pointer;
}

.scale-item label {
    font-size: 14px;
}

.scale-labels {
    display: flex;
    justify-content: space-between;
    margin-top: 5px;
    font-size: 12px;
    color: #666;
}
</style>