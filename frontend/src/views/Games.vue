<template>
  <div class="game-list-container">
    <div class="game-list-header">
      <div class="game-list-title">
        <h2 v-if="!showGameDetailSidebar">
          P. Alexander's Compendium of the Marvellous and Fantastic
        </h2>
        <h3 v-if="!showGameDetailSidebar">
          a Breviary of Catalogued Portals Into the Unseen Sights of Vivid Imagination
        </h3>
        <h2 v-if="showGameDetailSidebar">The Compendium</h2>
      </div>
      <div class="game-list-control-container">
        <button id="add-game-button" @click="showAddGameModal = true">
          <ph-plus-circle :size="30" />
        </button>
        <button id="refresh-game-list-button" @click="fetchGames(refresh = true)">
          <ph-arrow-counter-clockwise :size="30"/>
        </button>
    </div>
    </div>
    <div class="game-list-body" v-if="!!games" >
      <GameCard v-for="game in games"
                :key="game"
                :game="game"
                @cardClicked="toggleSidebar" />
    </div>
  </div>
  <div class="game-list-modal-container">
    <add-game-modal :show="showAddGameModal"
                    @closeModal="showAddGameModal = false" />
  </div>
  <div class="game-list-sidebar-container">
    <GameDetailSidebar :show="showGameDetailSidebar"
             @toggleSidebar="toggleSidebar"
             v-model:game="activeCard" />
  </div>
</template>v

<script>
import { mapActions } from 'vuex';
import GameCard from '@/components/GameCard.vue';
import AddGameModal from '@/components/AddGameModal.vue';
import GameDetailSidebar from '@/components/GameDetailSidebar.vue';

export default {
  name: 'Games',
  components: {
    GameCard,
    AddGameModal,
    GameDetailSidebar,
  },
  data() {
    return {
      showAddGameModal: false,
      showGameDetailSidebar: false,
      activeCard: null,
    };
  },
  computed: {
    games() {
      return this.$store.state.games.games;
    },
  },
  methods: {
    ...mapActions(['refreshGames', 'createGame', 'getGames']),
    toggleSidebar(game) {
      if (!this.activeCard) {
        this.activeCard = game;
        this.showGameDetailSidebar = !this.showGameDetailSidebar;
      } else if (game.id !== this.activeCard.id) {
        this.activeCard = game;
        if (!this.showGameDetailSidebar) { this.showGameDetailSidebar = true; }
      } else if (game.id === this.activeCard.id) {
        this.showGameDetailSidebar = !this.showGameDetailSidebar;
      }
    },
    async fetchGames(refresh = false) {
      if (!refresh && !!this.games) { return; }

      const { accessToken } = this.$store.state.auth;
      this.getGames(accessToken)
        .catch((error) => {
          if (error.msg === 'Token has expired') {
            this.$router.push('/login');
          }
          return error;
        });
    },
  },
  created() {
    this.fetchGames();
  },
};
</script>

<style scoped>
.game-list-container {
  height: 100%;
  width: 100%;
}

.game-list-header {
  display: grid;
  grid-template-columns: auto min-content;
  align-items: center;
  width: 100%;
}

.game-list-control-container {
  display: flex;
  align-items: left;
  width: min-content;
  margin-right: 1em;
}

.game-list-control-container > button {
  margin: 5px;
  background-color: transparent;
  border: none;
  height: min-content;
}

h2, h3 {
  text-align: center;
  margin-left: 2em;
}

h2 {
  font-size: large;
}

h3 {
  font-size: smaller;
}

.game-list-body {
  display: flex;
  height: min-content;
  justify-content: space-evenly;
  flex-wrap: wrap;
  grid-auto-rows: auto;
}

 .game-list-control-container > button:hover {
   color: #3185FC;
 }
</style>
