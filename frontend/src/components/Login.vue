<template>
  <div>
    <form id="login-form" @submit.prevent="submit">
      <h1>Log In</h1>
      <div>
        <label for="username" id="login-username-label">username</label>
        <input type="text"
              name="username"
              v-model="form.username"
              id="login-input-username"
              required />
      </div>
      <div>
        <label for="password" id="login-password-input">password</label>
        <input type="text"
              name="password"
              v-model="form.password"
              id="login-input-password"
              required />
      </div>
      <button type="submit">Log In</button>
      <p v-if="showError" id="error">Username or Password is incorrect.</p>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Login',
  data() {
    return {
      form: {
        username: null,
        password: null,
      },
      showError: false,
    };
  },
  methods: {
    ...mapActions(['LogIn']),
    async submit() {
      const User = new FormData();
      User.append('username', this.form.username);
      User.append('password', this.form.password);
      try {
        await this.LogIn(User);
        this.$router.push('/games');
        this.showError = false;
      } catch (error) {
        this.showError = true;
      }
    },
  },
};
</script>
