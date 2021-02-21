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
    const promise = axios.get('game/',
      { headers: { Authorization: `Bearer ${accessToken}` } });

    promise
      .then((res) => {
        const { data } = res;
        commit('setGames', data);
      }).catch((error) => error);

    return promise;
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
