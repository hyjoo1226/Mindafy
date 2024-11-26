<template>
    <div class="container mx-auto px-4 py-8">
        <!-- 메인 결과 섹션 -->
        <div v-if="result" class="bg-white rounded-lg shadow-lg p-6 mb-8">
            <h1 class="text-3xl font-bold text-center mb-6">{{ result.result_type }}</h1>
            
            <!-- 설명 섹션 -->
            <div class="mb-8">
                <p class="text-lg text-gray-700 mb-4">{{ result.description }}</p>
                <div class="bg-blue-50 p-4 rounded-lg">
                    <p class="text-blue-800">{{ result.match }}</p>
                </div>
            </div>

            <!-- 점수 표시 및 그래프 -->
            <div class="grid grid-cols-2 gap-4 mb-8">
                <div class="bg-gray-50 p-4 rounded-lg text-center">
                    <h3 class="font-semibold mb-2">위험 회피 점수</h3>
                    <p class="text-2xl text-blue-600">{{ result.risk_total }} / 105</p>
                </div>
                <div class="bg-gray-50 p-4 rounded-lg text-center">
                    <h3 class="font-semibold mb-2">자극 추구 점수</h3>
                    <p class="text-2xl text-blue-600">{{ result.stimulus_total }} / 105</p>
                </div>
            </div>
            
            <!-- 그래프 추가 -->
            <div class="mb-8">
                <canvas id="scoreChart"></canvas>
            </div>

            <!-- 추천 상품 섹션 (기존 코드와 동일) -->
            <!-- 추천 상품 섹션 -->
            <div v-if="result.products?.length" class="mt-8">
                <h2 class="text-2xl font-bold mb-4">추천 금융 상품</h2>
                <div v-for="(productData, index) in result.products" :key="index" 
                     class="border rounded-lg p-4 mb-4">
                    <h3 class="text-xl font-semibold mb-2">
                        {{ productData.product.fin_prdt_nm }}
                    </h3>
                    <p class="text-gray-600 mb-2">{{ productData.product.kor_co_nm }}</p>
                    
                    <!-- 상품 옵션 테이블 -->
                    <div class="overflow-x-auto">
                        <table class="w-full mt-4">
                            <thead>
                                <tr class="bg-gray-50">
                                    <th class="px-4 py-2">저축 기간(개월)</th>
                                    <th class="px-4 py-2">기본금리(%)</th>
                                    <th class="px-4 py-2">우대금리(%)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="option in productData.options" :key="option.id"
                                    class="border-t">
                                    <td class="px-4 py-2 text-center">{{ option.save_trm }}</td>
                                    <td class="px-4 py-2 text-center">{{ option.intr_rate }}</td>
                                    <td class="px-4 py-2 text-center">{{ option.intr_rate2 }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- 추가 정보 -->
                    <div class="mt-4 text-sm text-gray-600">
                        <p v-if="productData.product.etc_note" class="mb-2">
                            <strong>참고사항:</strong> {{ productData.product.etc_note }}
                        </p>
                        <p v-if="productData.product.mtrt_int" class="mb-2">
                            <strong>만기 이자:</strong> {{ productData.product.mtrt_int }}
                        </p>
                    </div>
                </div>
            </div>
            <!-- ... -->
        </div>
        <div v-else class="text-center py-8">
            <p class="text-gray-600">결과를 불러오는 중입니다...</p>
        </div>
    </div>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import Chart from 'chart.js/auto';

const store = useCounterStore();
const result = computed(() => store.testResult);

onMounted(() => {
    if (result.value) {
        const ctx = document.getElementById('scoreChart');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['위험 회피 점수', '자극 추구 점수'],
                datasets: [{
                    label: '점수',
                    data: [result.value.risk_total, result.value.stimulus_total],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.5)',
                        'rgba(54, 162, 235, 0.5)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 105
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: '위험 회피 점수 vs 자극 추구 점수'
                    }
                }
            }
        });
    }
});
</script>

<style scoped>
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem 1rem;
    text-align: center; /* Mindafy 로고 중앙 정렬을 위해 추가 */
}

h1 {
    color: #2c3e50;
    margin-bottom: 1.5rem;
    display: inline-block; /* 로고 텍스트만 중앙 정렬을 위해 추가 */
}

h2 {
    color: #34495e;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

.bg-white {
    background-color: #ffffff;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 0.5rem;
    padding: 1.5rem;
}

.text-blue-600 {
    color: #3498db;
}

.bg-blue-50 {
    background-color: #e3f2fd;
}

.text-blue-800 {
    color: #1565c0;
}

.bg-gray-50 {
    background-color: #f8fafc;
}

.border {
    border-color: #e2e8f0;
}

/* 그래프 섹션에 여백 추가 */
.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin: 0 auto;
    max-width: 80%; /* 그래프 섹션의 최대 너비 제한 */
}

table {
    border-collapse: separate;
    border-spacing: 0;
    width: 100%;
}

th, td {
    border: 1px solid #e2e8f0;
    padding: 0.75rem 1rem;
    text-align: left;
}

th {
    background-color: #f1f5f9;
    font-weight: 600;
    color: #475569;
}

th:first-child {
    border-top-left-radius: 0.375rem;
}

th:last-child {
    border-top-right-radius: 0.375rem;
}

tr:last-child td:first-child {
    border-bottom-left-radius: 0.375rem;
}

tr:last-child td:last-child {
    border-bottom-right-radius: 0.375rem;
}

.text-gray-600 {
    color: #718096;
}

.font-semibold {
    font-weight: 600;
}

.rounded-lg {
    border-radius: 0.5rem;
}

.shadow-lg {
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.overflow-x-auto {
    overflow-x: auto;
}

@media (max-width: 640px) {
    .container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .grid {
        grid-template-columns: 1fr;
    }
}
</style>