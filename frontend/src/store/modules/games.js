import axios from 'axios';

const state = {
  games: null,
};

const getters = {
};

const actions = {
  async getGames({ commit }, accessToken) {
    const response = await axios.get('game/',
      { headers: { Authorization: `Bearer ${accessToken}` } });
    await commit('setGames', response.data);
  },
};

const mutations = {
  /* eslint-disable-next-line */
  setGames(state, data) {
    state.games = data;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
