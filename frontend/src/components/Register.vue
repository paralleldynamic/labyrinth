<template>
  <div class="form-container">
    <form id="login-form" @submit.prevent="submit">
      <h1>the labyrinth</h1>
      <div class="input-container">
        <div>
          <input type="text"
                name="username"
                placeholder="username"
                v-model="form.username"
                id="register-input-username"
                required />
        </div>
        <div>
          <input type="email"
                name="email"
                placeholder="email"
                v-model="form.email"
                id="register-input-email"
                required />
        </div>
        <div>
          <input type="password"
                name="password"
                placeholder="password"
                v-model="form.password"
                id="register-input-password"
                required />
        </div>
        <div>
          <input type="password"
                name="password-confirmation"
                placeholder="confirm password"
                v-model="form.passwordConfirmation"
                id="register-input-confirm-password"
                required />
        </div>
        <div>
          <input type="text"
                name="invitation_code"
                placeholder="invitation code"
                v-model="form.invitationCode"
                id="login-input-password"
                required />
        </div>
      </div>
      <button type="submit">Log In</button>
      <p v-if="showError" id="error">Username or Password is incorrect.</p>
    </form>
    <div class='login-form-nav'>
      <router-link class="link-to-register" to="/register">Have an account? Log in.</router-link>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Register',
  data() {
    return {
      form: {
        username: null,
        password: null,
        passwordConfirmation: null,
        invitationCode: null,
      },
      showError: false,
    };
  },
  methods: {
    ...mapActions(['login']),
    async submit() {
      const User = new FormData();
      User.append('username', this.form.username);
      User.append('email', this.form.email);
      User.append('password', this.form.password);
      try {
        await this.login(User);
        await this.$router.push('/games');
        this.showError = false;
      } catch (error) {
        this.showError = true;
      }
    },
  },
};
</script>

<style>
body {
  background-color: #FBFBFF;
}
</style>

<style scoped>
.form-container {
  background-color: #FBFBFF;
  border-radius: 5px;
  box-shadow: 0 2px 5px #19191950;
  margin: 3rem auto 5rem auto;
  width: 30rem;
  text-align: center;
}

.login-form-nav {
  margin: 0.5em;
  padding: 1em;
}

.link-to-login {
  color: #3185FC;
}

h1 {
  padding: 1rem;
  margin: 1rem;
  margin-bottom: 0;
}

.input-container {
  margin-bottom: 0.75rem;
}

input {
  width: 90%;
  padding: 0.25rem;
  margin: 0.5rem auto 0.5rem auto;
  background: #FBFBFF;
  border-width: 1px;
  border-radius: 5px;
}

</style>
