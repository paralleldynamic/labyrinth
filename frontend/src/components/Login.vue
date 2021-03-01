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
                id="login-input-username"
                required />
        </div>
        <div>
          <input type="password"
                name="password"
                placeholder="password"
                v-model="form.password"
                id="login-input-password"
                required />
        </div>
      </div>
      <button type="submit">Log In</button>
      <strong><em><p v-if="showError"
                     class="error-message"
                     id="registration-error">{{ responseMessage }}</p></em></strong>
    </form>
    <div class='login-form-nav'>
      <router-link class="link-to-register" to="/register">Not registered?</router-link>
    </div>
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
      responseMessage: null,
    };
  },
  methods: {
    ...mapActions(['login']),
    async submit() {
      const User = new FormData();
      User.append('username', this.form.username);
      User.append('password', this.form.password);
      await this.login(User)
        .then(() => {
          this.$router.push('/games');
        })
        .catch((error) => {
          this.responseMessage = error.response.data.message;
          this.showError = true;
        });
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

.link-to-register {
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

.error-message {
  font-size: smaller;
  margin: 0;
  padding-left: 2em;
  text-align: left;
  color: #F03A47;
}

#registration-error {
  margin-top: 1em;
  padding-left: 0;
  text-align: center;
}
</style>
