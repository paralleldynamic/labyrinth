<template>
  <div class="game-list-container">
    <div class="header-title">
      <h2>P Alexander's Compendium of the Marvellous and Fantastic</h2>
      <h3>a Breviary of Catalogued Portals Into the Unseen Sights of Vivid Imagination</h3>
    </div>
    <div id="game-list-control-container">
        <button id="add-game-button" @click="showAddGameModal = true">
          <ph-plus-circle :size="30" />
        </button>
        <button id="refresh-game-list-button" hidden>
          <ph-arrow-counter-clockwise :size="30"/>
        </button>
    </div>
    <div class="card-container">
      <ContentCards />
    </div>
    <div class="modal-container">
      <add-game-modal id="add-game-form"
             :show="showAddGameModal"
             @close="showAddGameModal = false" />
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import ContentCards from '@/components/ContentCards.vue';
import AddGameModal from '@/components/AddGameModal.vue';

export default {
  name: 'Games',
  components: {
    ContentCards,
    AddGameModal,
  },
  data() {
    return {
      showAddGameModal: false,
    };
  },
  methods: {
    ...mapActions(['refreshGames', 'createGame']),
  },
};
</script>

<style scoped>
.game-list-container {
  margin: auto;
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
  width: 100%;
}

.header-title {
  margin: 0 0 1em 0;
}

#game-list-control-container {
  position: absolute;
  right: 1.5em;
  top: calc(var(--header-container-height) + 1.5em);
}

#game-list-control-container button {
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

.card-container {
  display: flex;
  align-items: space-between;
  justify-content: space-evenly;
  flex-wrap: wrap;
  grid-template-columns: repeat(autofill, 1fr);
  grid-auto-rows: auto;
}
</style>
