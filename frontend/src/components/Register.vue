<template>
  <div class="form-container">
    <form id="registration-form" @submit.prevent="submit">
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
          <p v-if="form.password != form.passwordConfirmation"
             class="error-message">
              <strong><em>Password entries must match.</em></strong>
          </p>
        </div>
        <div>
          <input type="text"
                name="invitation_code"
                placeholder="invitation code"
                v-model="form.invitationCode"
                id="login-input-invitation-code"
                required />
        </div>
      </div>
      <button type="submit">Register</button>
      <strong><em><p v-if="showError"
                     class="error-message"
                     id="registration-error">{{ responseMessage }}</p></em></strong>
    </form>
    <div class='registration-form-nav'>
      <router-link class="link-to-login" to="/login">Have an account? Log in.</router-link>
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
      responseMessage: null,
    };
  },
  methods: {
    ...mapActions(['login', 'register']),
    async submit() {
      this.responseMessage = null;
      const Registration = new FormData();
      Registration.append('username', this.form.username);
      Registration.append('email', this.form.email);
      Registration.append('password', this.form.password);
      Registration.append('invitation_code', this.form.invitationCode);
      await this.register(Registration)
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

.registration-form-nav {
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
