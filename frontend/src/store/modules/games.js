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
  async postGame({ commit }, { Game, accessToken }) {
    console.log('made it to function');
    const promise = axios.post('game/',
      Game,
      { headers: { Authorization: `Bearer ${accessToken}` } });

    promise
      .then((res) => {
        const { data } = res;
        commit('addGame', data);
      }).catch((error) => error);

    return promise;
  },
};

const mutations = {
  /* eslint-disable-next-line */
  setGames(state, data) {
    state.games = data;
  },
  /* eslint-disable-next-line */
  addGame(state, data) {
    console.log('before: ' && state.games);
    state.games.push(data);
    console.log('after: ' && state.games);
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
