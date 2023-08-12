import { createRouter, createWebHistory } from 'vue-router'
import Home from '.././components/HomePage.vue'
import Login from '.././components/LoginPage.vue'
import Rankings from '.././components/RankingPage.vue'
import List from '.././components/CardList.vue'
const router = createRouter({
    history: createWebHistory(),
    routes:[
    {
        path: '/',
        component: Home
    },
    {
        path:'/loginPage',
        component: Login
    },
    {
        path:'/Rankings',
        component: Rankings
    },
    {
        path:'/cardList',
        component: List
    },
]
})

export default router