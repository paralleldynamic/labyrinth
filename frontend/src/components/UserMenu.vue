<template>
  <div class="user-menu">
    <button class="user-menu-dropdown-button"><ph-user-circle :size="25" /></button>
    <div class="user-menu-dropdown-content">
      <router-link class="user-menu-dropdown-item" to="/logout">Logout</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserMenu',
};
</script>

<style scoped>
.user-menu {
  float: right;
  overflow: hidden;
  background-color: #FBFBFF;
}

button {
  background-color: transparent;
  border: 0;
}

.user-menu-dropdown-content {
  display: none;
  position: absolute;
  right: 2%;
  background-color: #FBFBFF;
  box-shadow: 1px 1px 1px #191919;
  min-width: 15%;
  z-index: 1;
}

.user-menu-dropdown-content a {
  float: none;
  color: #191919;
  text-decoration: none;
  display: block;
  text-align: center;
  padding: 0.5em;
}

.user-menu:hover .user-menu-dropdown-content {
  display: block;
  border: 10px;
  border-radius: 1x;
}
</style>
