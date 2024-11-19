import DetailView from '@/views/DetailView.vue'
import StartView from '@/views/StartView.vue'
import SurveyView from '@/views/SurveyView.vue'
import TestView from '@/views/TestView.vue'
import UserView from '@/views/UserView.vue'
import { createRouter, createWebHistory } from 'vue-router'


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
      component:UserView
    },
    {
      path:'/detail/:testname',
      name:'detail',
      component: DetailView,
      props: true, // 활성화
    },
    {
      path:'/survey',
      name:'survey',
      component: SurveyView
    },
  ],
})

export default router
