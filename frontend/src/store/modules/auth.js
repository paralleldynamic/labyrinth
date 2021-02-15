import axios from 'axios';

const state = {
  user: null,
  games: null,
};

const getters = {
  isAuthenticated: () => !!state.user,
  StateGames: () => state.games,
  StateUser: () => state.user,
};

const actions = {
  async Register({ dispatch }, form) {
    await axios.post('register', form);
    const UserForm = new FormData();
    UserForm.append('username', form.username);
    UserForm.append('password', form.password);
    await dispatch('LogIn', UserForm);
  },
  async LogIn({ commit }, User) {
    const response = await axios.post('user/login', User);
    console.log(response.headers);
    await commit('setUser', User.get('username'));
  },
  async LogOut({ commit }) {
    const user = null;
    commit('logout', user);
  },
  async PostGame({ dispatch }, game) {
    await axios.post('game', game);
    await dispatch('GetGames');
  },
  async GetGames({ commit }) {
    const response = await axios.get('game');
    commit('setGame', response.data);
  },
};

const mutations = {
  // TODO: refactor functions so they aren't "shadowing" global variable state
  /* eslint-disable-next-line */
  setUser(state, username) {
    state.user = username;
  },
  /* eslint-disable-next-line */
  setGames(state, games) {
    state.games = games;
  },
  /* eslint-disable-next-line */
  LogOut(state) {
    state.user = null;
    state.posts = null;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
