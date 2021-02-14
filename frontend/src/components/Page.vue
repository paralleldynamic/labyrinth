<template>
  <HeaderContainer />
  <div id="page-content">
    <router-view />
  </div>
  <FooterContainer />
</template>

<script>
import HeaderContainer from '@/components/HeaderContainer.vue';
import FooterContainer from '@/components/FooterContainer.vue';

export default {
  components: {
    HeaderContainer,
    FooterContainer,
  },
};
</script>

<style scoped>
#page-content {
  margin-top: var(--header-container-height);
  margin-bottom: var(--footer-container-height);
  height: 100%;
  display: flex;
  align-items: stretch;
}
</style>
