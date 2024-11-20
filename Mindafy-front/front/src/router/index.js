import DetailView from '@/views/DetailView.vue'
import LogInView from '@/views/LogInView.vue'
import SignUpView from '@/views/SignUpView.vue'
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
      path:'/tests/:id',
      name:'detail',
      component: DetailView,
    },
    // {
    //   path:'/survey/:id',
    //   name:'survey',
    //   component: SurveyView
    // },
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

export default router
