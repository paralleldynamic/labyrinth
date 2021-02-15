import axios from 'axios';

const state = {
  username: null,
  accessToken: null,
  authenticated: null,
};

const getters = {
  /* eslint-disable-next-line */
  authenticated: (state) => !!state.username && !!state.accessToken,
};

const actions = {
  async login({ commit }, User) {
    const response = await axios.post('user/login', User);
    await commit('loginUser', response.data);
  },
  async logout({ commit }) {
    commit('logout', null);
  },
};

const mutations = {
  // TODO: refactor functions so they aren't "shadowing" global variable state
  /* eslint-disable-next-line */
  loginUser(state, data) {
    state.username = data.username;
    state.accessToken = data.access_token;
  },
  /* eslint-disable-next-line */
  logoutUser(state) {
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
