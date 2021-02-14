import { createRouter, createWebHistory } from 'vue-router';
import Atrium from '@/views/Atrium.vue';
import Login from '@/components/Login.vue';
import Page from '@/components/Page.vue';
import Register from '@/components/Register.vue';

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
        auth: true,
      },
      {
        path: 'about',
        name: 'About',
        component: () => import('@/views/About.vue'),
        auth: true,
      },
      {
        path: 'campaigns',
        name: 'Campaigns',
        component: () => import('@/views/Campaigns.vue'),
        auth: true,
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

export default router;
