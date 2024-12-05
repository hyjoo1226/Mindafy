<!-- TestView.vue -->
<template>
    <div class="container">
        <nav>
            <div class="nav-links">
                <RouterLink :to="{name:'user'}">MyPage</RouterLink>|
                
                <RouterLink :to="{name:'signup'}">SignUp</RouterLink>|
                
                <RouterLink :to="{name:'login'}">LogIn</RouterLink>
            </div>
            <LogOut/>
        </nav>
        <!-- <h1>TestPage</h1> -->
        <TestList/>
    </div>
</template>

<script setup>
import LogOut from '@/components/LogOut.vue';
import TestList from '@/components/TestList.vue';
import { useCounterStore } from '@/stores/counter';
import { onMounted } from 'vue'
const store = useCounterStore()
onMounted(()=>{
    store.getTests()
})
</script>

<style scoped>
.container {
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

.nav-links {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
}

.nav-links a {
    color: #1D63FF;
    text-decoration: none;
    padding: 0 15px;
    position: relative;
}

.nav-links span {
    color: #ccc;
    margin: 0 5px;
}

.nav-links a:not(:last-child)::after {
    content: '|';
    position: absolute;
    right: -5px;
    color: #ccc;
}

h1 {
    color: #333333;
}

@media (max-width: 768px) {
    nav {
        flex-direction: column;
        align-items: flex-start;
    }

    .nav-links {
        margin-top: 10px;
    }

    .nav-links a {
        margin-bottom: 10px;
    }
}
</style>