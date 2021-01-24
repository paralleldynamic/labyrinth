<template>
  <div class="card">
    <header class="card-header">
      <a href="https://eclipsephase.com/">
        <img id="eclipse-phase-logo" class="card-logo" src="https://eclipsephase.com/sites/all/themes/eclipse/logo.png" alt="eclipse phase logo">
      </a>
    </header>
    <h2 class="card-title">eclipse phase</h2>
    <p class="card-tagline">a game of transhuman horror</p>
  </div>
  <div class="card">
    <a href="https://www.fantasyflightgames.com/en/products/genesys/">
      <img id="genesys-logo" class="card-logo" src="https://images-cdn.fantasyflightgames.com/filer_public/70/67/7067c9e1-60bb-49ae-9b11-7d6e7926961d/gns01_anc_slider.jpg" alt="genesys logo">
    </a>
    <h2 class="card-title">Genesys</h2>
    <p class="card-tagline">a universal RPG based around narrative control</p>
  </div>
</template>

<script>
export default {
  name: 'ContentCard',
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

#eclipse-phase-logo {
  background-color: black;
}
</style>
