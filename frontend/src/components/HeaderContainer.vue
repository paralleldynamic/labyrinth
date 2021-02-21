<template>
  <div id="header-container">
    <header>
      <div class="header-left">
        <ph-list id="site-menu" :size="20" />
      </div>
      <div class="header-center">
        <nav id="navbar-menu">
          <div>
            <h1 id="navbar-title">the labyrinth</h1>
          </div>
          <div id="navbar-menu-items-container">
            <router-link class="navbar-menu-item" to="/games">Games</router-link>
            <router-link class="navbar-menu-item" to="/campaigns">Campaigns</router-link>
            <router-link class="navbar-menu-item" to="/about">About</router-link>
          </div>
        </nav>
      </div>
      <div class="header-right">
        <UserMenu />
      </div>
    </header>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import UserMenu from '@/components/UserMenu.vue';

export default {
  name: 'HeaderContainer',
  components: {
    UserMenu,
  },
  computed: {
    ...mapGetters(['authenticated']),
  },
  methods: {
  },
};
</script>

<style scoped>
header {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-evenly;
}

#header-container {
  background-color: #FBFBFF;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: var(--header-container-height);
  box-shadow: 0 1px 2px #191919;
}

.header-left {
  flex: 1;
  text-align: left;
  margin-top: 0.5em;
  margin-left: 2em;
  margin-right: -2em;
}

.header-right {
  flex: 1;
  text-align: right;
  margin-top: 0.5em;
  margin-left: -2em;
  margin-right: 2em;
}

.header-center {
  flex: 4
}

#navbar-title {
  margin: 0.25em;
  margin-bottom: 0.4em;

  text-transform: lowercase;
}
#navbar-menu {
  display: block;
  font-size: small;
  text-transform: lowercase;
  text-align: center;
}

#navbar-menu-items-container {

}

.navbar-menu-item {
  display: inline;
  margin: 0.5em;
  text-decoration: none;
  color: inherit;
}

.navbar-menu-item:hover {
  font-size: smaller;
  font-weight: bolder;
}
</style>
