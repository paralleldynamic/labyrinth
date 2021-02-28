<template>
  <modal :show="show" @close="close">
    <div class="form-container">
      <form id="add-game-form" @submit.prevent="submit">
        <h1 class="form-name">add new game</h1>
        <div class="input-container">
          <label for="title">Game</label>
          <input type="text"
                name="title"
                placeholder="title"
                v-model="form.title"
                id="add-game-input-title"
                required />
          <label for="publisher_website">Publisher Website</label>
          <input type="text"
                name="publisher_website"
                placeholder="publisher website"
                v-model="form.publisher_website"
                id="add-game-input-publisher_website"
                required />
          <label for="logo_img_src">Logo URL</label>
          <input type="text"
                name="logo_img_src"
                placeholder="URL for game logo"
                v-model="form.logo_img_src"
                id="add-game-input-logo_img_src"
                required />
          <label for="logo_img_alt">Logo Alt Text</label>
          <input type="text"
                name="logo_img_alt"
                placeholder="alt text description for logo"
                v-model="form.logo_img_alt"
                id="add-game-input-logo_img_alt"
                required />
          <label for="tagline">Game Tagline</label>
          <input type="text"
                name="tagline"
                placeholder="tagline"
                v-model="form.tagline"
                id="add-game-input-tagline"
                required />
        <button type="submit">submit</button>
        </div>
      </form>
    </div>
  </modal>
</template>

<script>
import Modal from './Modal.vue';

export default {
  components: { Modal },
  props: [
    'show',
  ],
  data() {
    return {
      form: {
        title: null,
        publisher_website: null,
        logo_img_src: null,
        logo_img_alt: null,
        tagline: null,
      },
    };
  },
  methods: {
    close() {
      const f = this.form;
      Object.keys(f).forEach((k) => {
        f[k] = null;
      });
      this.$emit('close');
    },
  },
};
</script>

<style scoped>
.form-container {
  height: 100%;
}

.form-name {
  text-align: center;
}

.input-container {
  display: grid;
  grid-template-columns: auto auto;
}

label {
  font-size: medium;
  font-weight: bold;
  text-align: center;
  margin: 0.5em 1em 0.5em 0;
}

input {
  margin: 0.5em 1em 0.5em 0;
}

button {
  grid-column: 1 / 3;
  margin-top: 1.5em;
}
</style>
