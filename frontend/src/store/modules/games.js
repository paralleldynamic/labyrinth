import axios from 'axios';

const state = {
  games: null,
};

const getters = {
  // eslint-disable-next-line
  gamesPopulated: (state) => !!state.games,
};

const actions = {
  async getGames({ commit }, accessToken) {
    return axios.get('game/', { headers: { Authorization: `Bearer ${accessToken}` } })
      .then((res) => {
        const { data } = res;
        commit('setGames', data);
      });
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
