<template>
  <nav>
  <div id="app">
    <!-- Router -->
    <v-card class="overflow-hidden">
    <v-app-bar
      
      color="#6A76AB"
      dark
      shrink-on-scroll
      prominent
      src="./assets/Horizontal.jpg"
      fade-img-on-scroll
      scroll-target="#scrolling-techniques-4"
    >
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(10,115,201,.7), rgba(25,32,72,.7)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>CRYPTO</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-menu
        bottom
        left
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            icon
            color="yellow"
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item>
            <v-list-item-title>Click Me 1</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <template v-slot:extension>
        <v-tabs align-with-title>

          <v-tab @click="redirectToUser">INICIO</v-tab>
          <v-tab @click="redirectToLogin">LOGIN</v-tab>
          <v-tab @click="redirectToData">USUARIOS</v-tab>

<!--
          <v-tab @click="redirectToWebCamm">Criptomonedas</v-tab>
           
          <v-tab @click="redirectToCurso">CURSO</v-tab>
          <v-tab @click="redirectToHorario">HORARIO</v-tab>
          <v-tab @click="redirectToDocentes">DOCENTE</v-tab>

          <v-tab @click="redirectToWebCam">Tab 3</v-tab>

          <v-tab @click="redirectToAlumno">Alumno</v-tab>
          <v-tab @click="redirectToParticipacion">Participacion</v-tab>
          -->
          <!--    
          <v-tab @click="redirectToJustificacion">Justificacion</v-tab>
          <v-tab @click="redirectToAsistencia">Asistencia</v-tab>

          <v-tab>Tab 3</v-tab>

          -->
          <v-tab>Tab 3</v-tab>

        </v-tabs>
        
      </template>
 
    </v-app-bar>

    <v-sheet
      id="scrolling-techniques-3"
      class="overflow-y-auto"
      max-height="600"
    >
      <v-container style="height: 100px;"></v-container>
    </v-sheet>
    <router-view></router-view> <!-- Esto se remplaza segun el componente seleccionado en el router-->

  </v-card>
    <!-- fin Router -->
  </div>


</nav>


</template>

<script>


export default {
  name: 'App',
  methods: {
    redirectToWebCamm() {
           this.$router.push('/webcamm')

      },
    redirectToUser() {
           this.$router.push('/')

      },
    redirectToData() {
           this.$router.push('/usuarios')

      },
      redirectToCurso() {
           this.$router.push('/cursos')

      },
      redirectToDocentes() {
           this.$router.push('/docente')

          },
      redirectToTipoUsuarios() {
           this.$router.push('/tipo_usuarios')


          },
      redirectToWebCam() {
           this.$router.push('/webcam')

          },
      redirecttoEjemplo() {
           this.$router.push('/CmpEjem')

          },
          redirectToHorario() {
           this.$router.push('/horario')
          },
          redirectToAlumno() {
           this.$router.push('/alumno')
          },
          redirectToParticipacion() {
           this.$router.push('/participacion')
          },
          redirectToJustificacion() {
           this.$router.push('/justificacion')
          },
          redirectToAsistencia() {
           this.$router.push('/asistencia')
          },
          redirectToLogin() {
           this.$router.push('/login')
          }

          
    },

  components: {
    //HelloWorld
    
    
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  text-align: center;
  color: #697178;
  margin-top: 0px;
}
</style>