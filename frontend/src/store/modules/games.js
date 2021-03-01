/* eslint no-shadow: ["error", { "allow": ["state"] }] */

import axios from 'axios';

const state = {
  games: null,
};

const getters = {
  gamesPopulated: (state) => !!state.games,
};

const actions = {
  async getGames({ commit }, accessToken) {
    if (state.games) { state.games = null; }

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
    const promise = axios.post('game/',
      Game,
      { headers: { Authorization: `Bearer ${accessToken}` } });

    promise
      .then((res) => {
        const { game } = res.data;
        commit('addGame', game);
      }).catch((error) => error);

    return promise;
  },
  /* eslint-disable-next-line */
  async deleteGame({ commit }, { id, accessToken }) {
    const endpoint = `game/${id}`;
    const promise = axios.delete(endpoint,
      { headers: { Authorization: `Bearer ${accessToken}` } });

    promise
      .then(commit('deleteGame', id))
      .catch((error) => error);
    commit('deleteGame', id);
  },
};

const mutations = {
  setGames(state, data) {
    state.games = data;
  },
  addGame(state, game) {
    state.games.push(game);
  },
  deleteGame(state, id) {
    state.games = state.games.filter((game) => game.id !== id);
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
