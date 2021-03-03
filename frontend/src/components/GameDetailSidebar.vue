<template>
  <sidebar :show="show" @toggleSidebar="toggleSidebar">
    <template v-slot:sidebar-header>
      <img id="game-logo"
            v-bind:src="game.logo_img_src"
            v-bind:alt="game.logo_img_alt"
            v-bind:style="game.logo_img_style">
      <div v-if="!edit">
        <p>{{ game.tagline }}</p>
      </div>
    </template>
    <template v-slot:sidebar-content>
      <div class="sidebar-content-container" v-if="!edit">
        <h1>{{ game.title }}</h1>
        <div id="publisher-website">
          <p>Publisher Website:
            <a v-bind:href="game.publisher_website" target="_blank">
              {{ game.publisher ? game.publisher : "link to publisher" }}
            </a>
          </p>
        </div>
        <div id="extended-description">
          <p> {{ game.extended_description ? game.extended_description :
            `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
            incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
            exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
            dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
            mollit anim id est laborum.` }}
          </p>
        </div>
        <div id="scales">
        </div>
        <div id="tags">
          <p>universal</p>
          <p>narrative</p>
          <p>sandbox</p>
          <p>cinematic</p>
        </div>
      </div>
      <div class="sidebar-content-form" v-if="edit">
        <form id="add-game-sidebar-form" @submit.prevent="submit">
          <label for="title">Title</label>
          <input type="text"
                name="title"
                v-bind:placeholder="game.title ? game.title : 'title'"/>

          <label for="tagline">Tagline</label>
          <input type="text"
                name="tagline"
                v-bind:placeholder="game.tagline ? game.tagline : 'tagline'"/>

          <label for="game_website">Website for the game itself</label>
          <input type=""
                name="game_website"
                v-bind:placeholder=
                  "game.website ? game.website : 'game website'"/>

          <label for="publisher">Publisher</label>
          <input type="text"
                name="publisher"
                v-bind:placeholder="game.publisher ? game.publisher : 'publisher'"/>

          <label for="publisher_website">Publisher website URL</label>
          <input type=""
                name="publisher_website"
                v-bind:placeholder=
                  "game.publisher.website ? game.publisher.website : 'publisher website'"/>

          <label for="description">Description.</label>
          <textarea name="description"
                    rows="10"
                    cols="50">
            {{ game.description ? game.description : 'description' }}
          </textarea>
          <div id="scales">
          </div>
          <div id="tags">
          </div>
        </form>
      </div>
    </template>
    <template v-slot:sidebar-footer>
      <div class="sidebar-controls">
        <button @click="toggleEdit">
          <ph-pencil-line v-if="!edit" :size="24" />
          <ph-eraser v-if="edit" :size="24" />
        </button>
        <button @click="submitUpdate"
                v-if="edit">
          <ph-floppy-disk :size="24" />
        </button>
        <button @click="submitDelete"
                id="delete-button"
                v-if="edit">
          <ph-trash :size="24" />
        </button>
        <button @click="toggleSidebar(game)"
                v-if="true">
          <ph-x-circle :size="24" />
        </button>
      </div>
    </template>
  </sidebar>
</template>

<script>
import Sidebar from '@/components/Sidebar.vue';
import { mapActions } from 'vuex';

export default {
  name: 'GameDetailSidebar',
  components: {
    Sidebar,
  },
  data() {
    return {
      edit: false,
    };
  },
  props: [
    'show',
    'game',
  ],
  emit: [
    'toggleSidebar',
  ],
  methods: {
    ...mapActions(['deleteGame']),
    toggleSidebar(game) {
      this.$emit('toggleSidebar', game);
    },
    toggleEdit() {
      this.edit = !this.edit;
    },
    async submitDelete() {
      // const { id } = this.game;
      // const { accessToken } = this.$store.state.auth;
      // await this.deleteGame({ id, accessToken })
      //   .then(this.toggleSidebar(this.game))
      //   .catch((error) => error);
    },
  },
};
</script>

<style scoped>
#extended-description > p {
  margin: 0;
  padding: 0;
}

#game-logo {
  padding: 1em;
  box-sizing: content-box;
  background-color: #191919;
  max-width: 100%;
  max-height: 100%;
}

#extended-description {
  padding: 0.5em;
  margin: 0.5em;
  font-size: smaller;
  text-align: justify;
  text-justify: newspaper;
}

#add-game-sidebar-form {
  display: grid;
}

 #tags {
   display: flex;
 }

 .sidebar-controls > button {
   margin: 0 1em 0 1em;
   background-color: transparent;
   border: none;
 }

.sidebar-controls {
  height: 100%;
  display: flex;
  flex-wrap: nowrap;
  justify-content: center;
  align-items: center;
}

 .sidebar-controls > button:hover {
   color: #3185FC;
 }

 #delete-button:hover {
   color: #F03A47;
 }
</style>
