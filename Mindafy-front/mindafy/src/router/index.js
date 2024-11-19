// index.js
import MainPageView from '@/views/MainPageView.vue'
import SearchView from '@/views/SearchView.vue'
import TestListView from '@/views/TestListView.vue'
import UserView from '@/views/UserView.vue'
import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainPageView,
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView,
    },
    {
      path: '/testlist',
      name: 'testlist',
      component: TestListView,
    },
    {
      path: '/user/:name',
      name: 'user',
      component: UserView,
      props: true
    },
  ],
})

export default router
