<!-- SurveyListItemOp.vue -->
<template>
    <div class="question-options">
        <!-- Multiple choice options -->
        <div v-if="options && options.length > 0" class="multiple-choice">
            <div v-for="(option, index) in options" :key="option.id" class="option-item">
                <label class="option-label">
                    <input 
                        type="radio" 
                        :name="'question-' + props.surveyQ.id"
                        :value="index + 1"
                        v-model="selectedAnswer"
                        @change="emitAnswer"
                        class="form-radio"
                    >
                    <span class="option-text">{{ option.option_text }}</span>
                </label>
            </div>
        </div>

        <!-- 7-point scale -->
        <div v-else class="scale-rating">
            <div class="option-item">
                <p class="option-text"></p>
                <div class="scale-container">
                    <label v-for="n in 7" :key="n" class="scale-item">
                        <input 
                            type="radio" 
                            :id="`question-${props.surveyQ.id}-scale-${n}`"
                            :name="'question-' + props.surveyQ.id"
                            :value="n"
                            v-model="scaleValue"
                            @change="emitAnswer"
                        />
                        <span>{{ n }}</span>
                    </label>
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
    margin-bottom: 10px;
}

.option-label {
    display: block;
    padding: 15px 15px 15px 40px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s;
    position: relative;
}

.option-label:hover {
    background-color: #f0f0f0;
}

.form-radio {
    position: absolute;
    opacity: 0;
}

.option-label::before {
    content: '';
    position: absolute;
    left: 15px;
    top: 50%;
    transform: translateY(-50%);
    width: 20px;
    height: 20px;
    border: 2px solid #1D63FF;
    border-radius: 50%;
}

.form-radio:checked + .option-text {
    font-weight: bold;
    color: #1D63FF;
}

.form-radio:checked + .option-text::after {
    content: '';
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    width: 10px;
    height: 10px;
    background-color: #1D63FF;
    border-radius: 50%;
}

.scale-container {
    display: flex;
    justify-content: space-between;
    margin: 10px 0;
}

.scale-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    cursor: pointer;
}

.scale-item input[type="radio"] {
    display: none;
}

.scale-item span {
    padding: 10px;
    border: 1px solid #e0e0e0;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.3s, color 0.3s;
}

.scale-item input[type="radio"]:checked + span {
    background-color: #1D63FF;
    color: white;
}

.scale-labels {
    display: flex;
    justify-content: space-between;
    margin-top: 5px;
    font-size: 12px;
    color: #666;
}
</style>