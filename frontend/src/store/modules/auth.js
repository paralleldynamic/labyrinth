import axios from 'axios';

const state = {
  username: null,
  accessToken: null,
  authenticated: null,
};

const getters = {
  // eslint-disable-next-line
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
  // eslint-disable-next-line
  loginUser(state, data) {
    state.username = data.username;
    state.accessToken = data.access_token;
  },
  // eslint-disable-next-line
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
