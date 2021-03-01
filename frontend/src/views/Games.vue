<template>
  <div class="game-list-container">
    <div class="game-list-header">
      <div class="game-list-title">
        <h2>P. Alexander's Compendium of the Marvellous and Fantastic</h2>
        <h3>a Breviary of Catalogued Portals Into the Unseen Sights of Vivid Imagination</h3>
      </div>
      <div class="game-list-control-container">
        <button id="add-game-button" @click="showAddGameModal = true">
          <ph-plus-circle :size="30" />
        </button>
        <button id="refresh-game-list-button" hidden>
          <ph-arrow-counter-clockwise :size="30"/>
        </button>
    </div>
    </div>
    <div class="game-list-body">
      <ContentCards @cardClicked="toggleSidebar" />
    </div>
  </div>
  <div class="game-list-modal-container">
    <add-game-modal :show="showAddGameModal"
                    @closeModal="showAddGameModal = false" />
  </div>
  <div class="game-list-sidebar-container">
    <GameDetailSidebar :show="showGameDetailSidebar"
             @toggleSidebar="toggleSidebar"
             :card="activeCard" />
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import ContentCards from '@/components/ContentCards.vue';
import AddGameModal from '@/components/AddGameModal.vue';
import GameDetailSidebar from '@/components/GameDetailSidebar.vue';

export default {
  name: 'Games',
  components: {
    ContentCards,
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
  methods: {
    ...mapActions(['refreshGames', 'createGame']),
    toggleSidebar(card) {
      if (!this.activeCard) {
        this.activeCard = card;
        this.showGameDetailSidebar = !this.showGameDetailSidebar;
      } else if (card.id !== this.activeCard.id) {
        this.activeCard = card;
        if (!this.showGameDetailSidebar) { this.showGameDetailSidebar = true; }
      } else if (card.id === this.activeCard.id) {
        this.showGameDetailSidebar = !this.showGameDetailSidebar;
      }
    },
  },
};
</script>

<style scoped>
.game-list-container {
  display: flex;
  height: 100%;
  justify-content: space-evenly;
  flex-wrap: wrap;
}

.game-list-header {
  display: grid;
  grid-template-columns: auto min-content;
  width: 100%;
}

.game-list-title {
}

.game-list-control-container {
  /* position: absolute;
  right: 1.5em;
  top: calc(var(--header-container-height) + 1.5em); */
  display: flex;
  align-items: left;
  width: min-content;
}

.game-list-control-container button {
  margin: 5px;
  background-color: transparent;
  border: none;
}

h2, h3 {
  text-align: center;
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
</style>
