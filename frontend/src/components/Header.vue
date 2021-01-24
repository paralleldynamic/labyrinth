<template>
  <div id="header-container">
    <header>
      <nav id="navbar-menu">
        <div>
          <h1>the labyrinth</h1>
        </div>
        <router-link to="/">Homes</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/games">Games</router-link>
        <router-link to="/campaigns">Campaigns</router-link>
        <router-link to="/stories">Stories</router-link>
      </nav>
    </header>
  </div>
</template>

<script>
export default {
  name: 'Header',
  components: {
  },
};
</script>
