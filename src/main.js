import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import 'vuetify/dist/vuetify.min.css';


// para peticiones
import VueResource from 'vue-resource'
Vue.use(VueResource);

// para navegacion
import VueRouter from 'vue-router'
Vue.use(VueRouter);


//Defecto
Vue.config.productionTip = false
/*
new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
*/
//////////////////////////////////////////////////////////////////////
// para tener un router

import CmpData from './components/CmpData'
import CmpUser from './components/CmpUser'
import CmpCursos from './components/CmpCursos'
import CmpDocente from './components/CmpDocente'
import CmpTipoUsuario from './components/CmpTipoUsuario'
import CmpWebCam from './components/CmpWebCam'
import CmpEjem from './components/CmpEjem'
import CmpHorario from './components/CmpHorario'
import CmpWebCamm from './components/CmpWebCamm'
/////////////////////////////////////////////////
import CmpAsistencia from './components/CmpAsistencia'
import CmpJustificacion from './components/CmpJustificacion'
import CmpAlumno from './components/CmpAlumno'
import CmpParticipacion from './components/CmpParticipacion'
//////////////////////////////////////////////////
import CmpLogin from './components/CmpLogin'


const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { // primero muestra el componente User
      path: '/',
      component: CmpUser
    },
    { // componente Test
      path: '/usuarios',
      component: CmpData
    },
    { // componente Test
      path: '/cursos',
      component: CmpCursos
    },
    { // componente Test
      path: '/docente',
      component: CmpDocente
    },
    { // componente Test
      path: '/tipo_usuarios',
      component: CmpTipoUsuario
    },
    { // primero muestra el componente User
      path: '/webcam',
      component: CmpWebCam
    },
    { // primero muestra el componente User
      path: '/CmpEjem',
      component: CmpEjem
    },
    { // primero muestra el componente User
      path: '/horario',
      component: CmpHorario
    },
    { // primero muestra el componente User
      path: '/webcamm',
      component: CmpWebCamm
    },
    { // primero muestra el componente User
      path: '/asistencia',
      component: CmpAsistencia
    },
    { // primero muestra el componente User
      path: '/justificacion',
      component: CmpJustificacion
    },
    { // primero muestra el componente User
      path: '/alumno',
      component: CmpAlumno
    },
    { // primero muestra el componente User
      path: '/participacion',
      component: CmpParticipacion
    },
    { // primero muestra el componente User
      path: '/login',
      component: CmpLogin
    }
  ]
});
//////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////

Vue.config.productionTip = false

/* eslint-disable no-new */
/*new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})*/



// para que funcione con router
new Vue({
  vuetify,
  render: h => h(App),
  
  
  router,
  components: { App },
  template: '<App/>'
}).$mount('#app')


Vue.use(vuetify);





const cors = require('cors');

// Habilitar CORS para todas las solicitudes
Vue.use(cors());

App.use(cors());

// Resto de tu código de configuración y rutas
// ...

Vue.listen(5050, () => {
  console.log('Servidor escuchando en el puerto 5050');
});