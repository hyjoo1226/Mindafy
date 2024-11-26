<!-- resultETFView.vue -->
<!-- ResultETFView.vue -->
<template>
    <div class="container mx-auto px-4 py-8">
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
        
        <!-- 그래프 -->
        <div class="mb-8">
          <canvas id="scoreChart"></canvas>
        </div>
  
        <!-- 추천 ETF 상품 섹션 -->
        <div v-if="result.products?.length" class="mt-8">
          <h2 class="text-2xl font-bold mb-4">추천 ETF 상품</h2>
          <div class="overflow-x-auto">
            <table class="w-full mt-4">
              <thead>
                <tr class="bg-gray-50">
                  <th class="px-4 py-2">상품명</th>
                  <th class="px-4 py-2">등락률(%)</th>
                  <th class="px-4 py-2">거래량</th>
                  <th class="px-4 py-2">기초지수</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="product in result.products" :key="product.product.id" class="border-t">
                  <td class="px-4 py-2">{{ product.product.itmsNm }}</td>
                  <td class="px-4 py-2" :class="{'text-red-600': product.product.fltRt < 0, 'text-green-600': product.product.fltRt > 0}">
                    {{ product.product.fltRt.toFixed(2) }}
                  </td>
                  <td class="px-4 py-2">{{ product.product.trqu.toLocaleString() }}</td>
                  <td class="px-4 py-2">{{ product.product.bssIdxIdxNm }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div v-else class="text-center py-8">
        <p class="text-gray-600">결과를 불러오는 중입니다...</p>
      </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
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
}

h1, h2, h3 {
color: #2c3e50;
}

.bg-white {
background-color: #ffffff;
box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
border-radius: 0.5rem;
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

table {
border-collapse: separate;
border-spacing: 0;
width: 100%;
}

th, td {
border: 1px solid #e2e8f0;
padding: 0.75rem 1rem;
}

th {
background-color: #f1f5f9;
font-weight: 600;
color: #475569;
}

.rounded-lg {
border-radius: 0.5rem;
}

.shadow-lg {
box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

@media (max-width: 640px) {
.grid {
    grid-template-columns: 1fr;
}
}
</style>