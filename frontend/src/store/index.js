import { createStore } from 'vuex';
import auth from './modules/auth';
import games from './modules/games';

export default createStore({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    auth,
    games,
  },
  plugins: [
  ],
});
