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
export default {
  name: 'ContentCard',
  data() {
    return {
      cards: [],
    };
  },
  methods: {
    getCards() {
      const path = 'http://localhost:5000/games';
      this.axios.get(path)
        .then((res) => {
          this.cards = res.data.cards;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getCards();
  },
};
</script>

<style scoped>
.card {
  box-shadow: 0 5px 10px rgba(0,0,0,0.19);
  border-radius: 3px;
  width: 25%;
  padding: 0.25em;
  margin: 0.5em;
  background-color: #F2F3F4;
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
