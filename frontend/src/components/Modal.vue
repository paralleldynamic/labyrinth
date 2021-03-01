<template>
  <transition name="modal">
    <div class="modal-mask" @click="closeModal" v-if="show">
      <div class="modal-wrapper">
        <div class="modal-container" @click.stop>
          <slot />
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'Modal',
  props: [
    'show',
  ],
  mounted() {
    document.addEventListener('keydown', (e) => {
      if (this.show && e.code === 'Escape') {
        this.closeModal();
      }
    });
  },
  methods: {
    closeModal() {
      this.$emit('closeModal');
    },
  },
};
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #19191950;
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  padding: 20px 30px;
  min-width: max-content;
  max-width: max-content;
  height: 50%;
  margin: 0px auto;
  background-color: #FBFBFF;
  border-radius: 2px;
  box-shadow: 0 2px 8px #191919;
  transition: all 0.3s ease;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

</style>
