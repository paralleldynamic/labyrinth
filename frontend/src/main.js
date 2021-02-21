import { createApp } from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import PhosphorVue from 'phosphor-vue';
import App from './App.vue';
import store from './store';
import router from './router';

// TODO: environmentalization?
// TODO: add unit tests u slacker
// TODO: refactor to environment or a plugin or a config module
axios.defaults.baseURL = 'http://localhost:5000/api'; // TODO: configure with production/env details

createApp(App)
  .use(store)
  .use(router)
  .use(VueAxios, axios)
  .use(PhosphorVue)
  .mount('#app');
