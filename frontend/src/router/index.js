import { createRouter, createWebHistory } from 'vue-router';
import Atrium from '@/views/Atrium.vue';
import Login from '@/components/Login.vue';
import Page from '@/components/Page.vue';
import Register from '@/components/Register.vue';
import store from '../store';

const routes = [
  {
    path: '',
    name: 'Atrium',
    component: Atrium,
  },
  {
    path: '/',
    component: Page,
    children: [
      {
        path: 'games',
        name: 'Games',
        component: () => import('@/views/Games.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: 'about',
        name: 'About',
        component: () => import('@/views/About.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: 'campaigns',
        name: 'Campaigns',
        component: () => import('@/views/Campaigns.vue'),
        meta: { requiresAuth: true },
      },
    ],
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
});

export default router;
