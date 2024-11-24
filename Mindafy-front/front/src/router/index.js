// index.js
import DetailView from '@/views/DetailView.vue'
import LogInView from '@/views/LogInView.vue'
import SignUpView from '@/views/SignUpView.vue'
import StartView from '@/views/StartView.vue'
import SurveyView from '@/views/SurveyView.vue'
import TestView from '@/views/TestView.vue'
import UserView from '@/views/UserView.vue'
import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name:'start',
      component:StartView
    },
    {
      path:'/test',
      name:'test',
      component:TestView
    },
    {
      path:'/user',
      name:'user',
      component:UserView,
      beforeEnter: (to, from, next) => {
        const store = useCounterStore(); // Pinia store 사용
        if (!store.token) {
          alert('로그인이 필요합니다.')
          next({ name: 'login' }); // 로그인 페이지로 리디렉션
        } else {
          next(); // 정상적으로 UserView로 이동
        }
      }
    },
    {
      path:'/tests/:id',
      name:'detail',
      component: DetailView,
    },
    {
      path:'/tests/:id/surveys',
      name:'survey',
      component: SurveyView
    },
    {
      path:'/signup',
      name:'signup',
      component:SignUpView
    },
    {
      path:'/login',
      name:'login',
      component:LogInView
    }
  ],
})

// Navigation Guard
router.beforeEach((to, from, next) => {
  const store = useCounterStore(); // Pinia store 가져오기

  // 로그인 상태에서 접근을 제한할 페이지 (SignUpView, LogInView)
  const restrictedRoutes = ['signup', 'login'];

  if (restrictedRoutes.includes(to.name) && store.token) {
    // 로그인 상태에서 제한된 페이지로 접근 시
    // console.log('이미 로그인 상태입니다. 메인 페이지로 이동합니다.');
    alert('이미 로그인 상태입니다.')
    next({ name: 'test' }); // 메인 페이지로 리디렉션
  } else {
    next(); // 다음 라우트로 이동
  }
});

export default router
