// counter.js
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRoute, useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const keyword = ref('')  // 검색어 상태 추가

  const onSearchPage = function(){
      router.push({name:'search'})
  }
  const onUserPage = function(name){
      router.push({name:'user', params:{name:name}})
  }
  const onTestListPage = function(){
      router.push({name:'testlist'})
  }
  const search = function(newKeyword) {
    keyword.value = newKeyword  // 검색어 업데이트
    console.log(keyword.value);
    
}

  return { router, onSearchPage, onTestListPage, onUserPage, keyword, search }
})
