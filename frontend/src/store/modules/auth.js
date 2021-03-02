/* eslint no-shadow: ["error", { "allow": ["state"] }] */

import axios from 'axios';

const state = {
  username: null,
  accessToken: null,
  authenticated: null,
  userIsAdmin: false,
};

const getters = {
  authenticated: (state) => !!state.username && !!state.accessToken,
};

const actions = {
  async login({ commit }, User) {
    const promise = axios.post('user/login', User);

    promise
      .then((res) => {
        const { data } = res;
        commit('loginUser', data);
      }).catch((error) => error);

    return promise;
  },
  async logout({ commit }) {
    if (getters.authenticated) {
      await commit('logoutUser');
    }
  },
  async register({ commit }, Registration) {
    const promise = axios.post('user/register', Registration);

    promise
      .then((res) => {
        const { data } = res;
        commit('loginUser', data);
      }).catch((error) => error);

    return promise;
  },
};

const mutations = {
  // TODO: refactor functions so they aren't "shadowing" global variable state
  loginUser(state, data) {
    state.username = data.username;
    state.accessToken = data.access_token;
  },
  logoutUser(state) {
    state.user = null;
    state.accessToken = null;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
