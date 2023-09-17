<template>
    <v-container class="login-container">
      <v-row align="center" justify="center">
        <v-col cols="50" sm="1000" md="10000">
          <v-img src="@/assets/usuario.png" alt="User Image" max-height="100" max-width="100"></v-img>
        </v-col>
      </v-row>
      <br>
      
      <v-container fluid>
        <v-row>
          <v-col cols="12" sm="6">
            <v-text-field v-model="username" label="Usuario"></v-text-field>
          </v-col>
          
          <v-col cols="12" sm="6">
            <v-text-field
              v-model="password"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :rules="[rules.required, rules.min]"
              :type="show1 ? 'text' : 'password'"
              name="input-10-1"
              label="Contraseña"
              hint="Recuerda los dígitos de tu DNI"
              counter
              @click:append="show1 = !show1"
            ></v-text-field>
          </v-col>
        </v-row>
      </v-container>
      
      <a>¿Olvido su contraseña?</a><br/>
      
      <v-row align="center" justify="center">
        <v-col cols="64" sm="4" md="6">
          <v-img src="@/assets/facebook.svg" alt="Login using Facebook" max-height="50" max-width="50"></v-img>
        </v-col>
        <v-col cols="64" sm="4" md="6">
          <v-img src="@/assets/google.svg" alt="Login using Google" max-height="50" max-width="50"></v-img>
        </v-col>
      </v-row>
      
      <br>
      
      <v-btn @click="crearToken" color="secondary" dark class="mb-2" v-bind="attrs" v-on="on">Iniciar Sesión</v-btn>
    </v-container>
  </template>
  
  <style>
  .login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  </style>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        show1: false,
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
          emailMatch: () => (`The email and password you entered don't match`),
        },
        username: '',
        password: '',

        datos: {
            username: '',
            password: '',
            },
      };
    },
    methods: {
      printData() {
        const data = {
          username: this.username,
          password: this.password,
        };
        console.log(JSON.stringify(data));
      },

      crearToken() {

        const data = {
          username: this.username,
          password: this.password,
        };
        axios.post('http://localhost:5050/generate_token', data)
            .then(response => {
                console.log(response.data);
              alert(response.data);
            // Aquí puedes hacer uso del token como lo necesites
           })
          .catch(error => {
           console.error(error);
          });
     }

    },
  };
  </script>
  