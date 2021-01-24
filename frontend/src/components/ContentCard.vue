<template>
  <div class="card-container">
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
  </div>
</template>

<script>
export default {
  name: "ContentCard"
}
</script>

<style scoped>
  .card {
    box-shadow: 0 10px 20px rgba(0,0,0,0.19);
  }
</style>
