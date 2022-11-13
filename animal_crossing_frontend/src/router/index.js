import { createRouter, createWebHistory } from 'vue-router'
import ViewCollection from '../views/Collection.vue'
import ListUsers from '../views/Users.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: ListUsers 
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/users',
    name: 'ListUsers',
    component: ListUsers
  },
  {
    path: '/collection/:id',
    name: 'ViewCollection',
    component: ViewCollection 
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
