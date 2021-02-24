<template>
  <div class="card" v-for="card in cards" v-bind:key="card">
    <div class="card-header">
      <a v-bind:href="card.website">
        <img class="card-logo" v-bind:src="card.logo_img_src"
                               v-bind:alt="card.logo_img_alt"
                               v-bind:style="card.logo_img_style">
        </a>
    </div>
    <h2 class="card-title">{{ card.title }}</h2>
    <p class="card-tagline">{{ card.tagline }}</p>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'ContentCards',
  data() {
    return {
      cards: [],
    };
  },
  methods: {
    ...mapActions(['getGames']),
    async fetchCards() {
      const { accessToken } = this.$store.state.auth;
      await this.getGames(accessToken)
        .then(() => {
          this.cards = this.$store.state.games.games;
        })
        .catch((error) => {
          if (error.msg === 'Token has expired') {
            this.$router.push('/login');
          }
          return error;
        });
    },
  },
  created() {
    this.fetchCards();
  },
};
</script>

<style scoped>
.card {
  box-shadow: 0 5px 10px #191919;
  border-radius: 3px;
  box-sizing: border-box;
  max-width: 25%;
  padding: 0.25em;
  margin: 0.5em;
  background-color: #FBFBFF;
}

.card-title {
  text-align: center;
  font-size: medium;
}

.card-logo {
  border-radius: 3px;
  width: 85%;
  display: block;
  padding: 3px;
  margin: 0.5em;
  margin-left: auto;
  margin-right: auto;
}

.card-tagline {
  text-align: justify;
  font-size: smaller;
  margin: 0.5em;
}
</style>
