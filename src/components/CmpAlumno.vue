<template>
  <div>
    <v-data-table :items="alumnos" :headers="columnas" item-key="id_alumno">

      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>CRUD alumnos</v-toolbar-title>
          <v-divider class="mx-3" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="secondary" dark class="mb-2" v-bind="attrs" v-on="on">
                Nuevo alumno
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">Crear alumno</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field v-model="alumno.id_usuario" placeholder="Ingresa ID Usuario" label="ID Usuario"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field v-model="alumno.tipousr_id" placeholder="Ingresa Tipo Usuario" label="Tipo Usuario"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field v-model="alumno.anio_alumno" placeholder="Ingresa el Año" label="Año"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field v-model="alumno.carrera" placeholder="Ingresa la Carrera" label="Carrera"></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancelar</v-btn>
                <v-btn color="blue darken-1" text @click="createalumno">Crear</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          

          

          <v-dialog v-model="dialogEditaralumno" max-width="500px">
  <v-card>
    <v-card-title>
      <span class="headline">Editar alumno</span>
    </v-card-title>
    <v-card-text>
      <v-row>
        <v-col cols="12" sm="6" md="6">
        <v-text-field v-model="alumno.id_usuario" placeholder="Ingresa ID Usuario" label="ID Usuario"></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="6">
        <v-text-field v-model="alumno.tipousr_id" placeholder="Ingresa Tipo Usuario" label="Tipo Usuario"></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="6">
        <v-text-field v-model="alumno.id_alumno" placeholder="Ingresa ID Alumno" label="ID Alumno"></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="6">
        <v-text-field v-model="alumno.anio_alumno" placeholder="Ingresa Año" label="Año"></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="6">
        <v-text-field v-model="alumno.carrera" placeholder="Ingresa la Carrera" label="Carrera"></v-text-field>
        </v-col>
      </v-row>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="dialogEditaralumno = false">Cancelar</v-btn>
      <v-btn color="blue darken-1" text @click="updatealumno">Actualizar</v-btn>
    </v-card-actions>
  </v-card>
</v-dialog>
       

        </v-toolbar>
      </template>
            
      <!-- eslint-disable-next-line vue/valid-v-slot -->
      <template v-slot:item.actions="{ item }">
        <td>
          <v-icon
            small
            class="mr-2"
            @click="editaralumno(item)"
          >
            mdi-pencil
          </v-icon>
          <v-icon
            small
            @click="eliminaralumno(item)"
          >
            mdi-delete
          </v-icon>
        </td>
      </template>
    </v-data-table>

   
  </div>
</template>

<script>
import axios from 'axios';
export default {
  
  data() {
    
      return {
        
          dialog: false,
          dialogDelete: false,
          dialogEditaralumno: false,
          U_alumnos: [ { value: null, text: 'Seleccione una opción', disabled: true },
                        { value: '1', text: 'Administrador' },
                        { value: '2', text: 'Alumno' },
                        { value: '3', text: 'alumno' },
                      ],
          alumnos: [],
          selectedUser: null,
          alumno: {
            id_alumno:'',
            contrasena: '',
            nombre: '',
            apellido: '',
            dni: '',
            file: '',
            tipoalumno:'',
            id_usuario:'',
            tipousr_id:'',
            tipo_alumno:''
          },
          isDniReadOnly: true 
          
      };
  },
  methods:{
    close () {
      this.dialog = false
      
    },

    editaralumno(item) {
      this.alumno = { ...item };
      this.dialogEditaralumno = true;
    },
    

    createalumno() {
      const alumnoData = {
        id_usuario: this.alumno.id_usuario,
        anio_alumno: this.alumno.anio_alumno,
        tipousr_id: this.alumno.tipousr_id,
        carrera: this.alumno.carrera

      };

        axios.put('http://127.0.0.1:5050/alumno', alumnoData)
          .then(response => {
          // Aquí puedes manejar la respuesta del servidor
          console.log(response.data);
          // Cerrar el diálogo y actualizar la lista de alumnos si es necesario
          this.dialog = false;
          alert("alumno Creado")
        })
        .catch(error => {
          // Manejar el error
          console.error(error);
        });
    },



    
    updatealumno() {
    // Construir el objeto FormData con los datos del alumno
    const alumnoData = {
        id_alumno: this.alumno.id_alumno,
        id_usuario: this.alumno.id_usuario,
        anio_alumno: this.alumno.anio_alumno,
        tipousr_id: this.alumno.tipousr_id,
        carrera: this.alumno.carrera

      };

    

    // Realizar la solicitud al endpoint para actualizar el alumno
    axios.patch('http://127.0.0.1:5050/alumno', alumnoData)
      .then(response => {
        // La solicitud fue exitosa, realizar las acciones necesarias
        console.log('alumno actualizado:', response.data);
        alert("alumno Actualizado")

        // Aquí puedes realizar alguna acción adicional, como mostrar una notificación de éxito o recargar la lista de alumnos
        this.fetchalumnos();

        // Cerrar el diálogo de edición
        this.dialogEditaralumno = false;
      })
      .catch(error => {
        // Hubo un error al realizar la solicitud, manejar el error
        console.error('Error al actualizar el alumno:', error);
        // Aquí puedes mostrar una notificación de error o realizar alguna acción de manejo de errores
      });
  },

    eliminaralumno(item) {
      // Realiza la lógica para eliminar el alumno
      // Puedes utilizar el ID del alumno o cualquier otra propiedad única para identificarlo
      // Por ejemplo, si tienes un ID único para cada alumno, podrías hacer algo como:
      const alumnoId = item.id_alumno;
      
      // Luego, puedes hacer la llamada a la API para eliminar el alumno
      axios.delete('http://127.0.0.1:5050/alumno', { data: { id_alumno: alumnoId } })
      .then(response => {
        // Realizar cualquier acción adicional después de borrar el alumno
        console.log(response.data);
        this.actualizarListaalumnos(alumnoId);
        
      })
      .catch(error => {
        // Manejar el error
        console.error(error);
      });
    },
    
    actualizarListaalumnos(alumnoId) {
      const index = this.alumnos.findIndex(alumno => alumno.id_alumno === alumnoId);
      if (index !== -1) {
        this.alumnos.splice(index, 1);
      }
    },
    
  },

  computed: {
  alumnoTitle () {
    return this.editedIndex === -1 ? 'Nuevo alumno' : 'Editar alumno'
  },
  columnas() {
      return [
          { text: 'COD', value: 'id_alumno' },
          { text: 'DNI', value: 'dni' },
          { text: 'contrasena', value: 'contrasena' },
          { text: 'Apellido', value: 'apellido' },
          { text: 'Nombre', value: 'nombre' },
          { text: 'carrera', value: 'carrera' },
          { text: 'anio_alumno', value: 'anio_alumno' },
          { text: 'fotosistema', value: 'fotosistema' },
          { text: 'Acciones', value: 'actions', sortable: false }

          ];
      }
  },


  created() {
  axios.post('http://127.0.0.1:5050/alumnos')
    .then(response => {
      this.alumnos = response.data.map(alumno => {
      return {
            id_alumno:alumno.id_alumno,
            dni: alumno.dni,
            contrasena: alumno.contrasena,
            nombre: alumno.nombre,
            apellido: alumno.apellido,
            carrera: alumno.carrera,
            anio_alumno: alumno.anio_alumno,
            tipousr_id: alumno.tipousr_id,
            id_usuario: alumno.id_usuario,
            fotosistema : alumno.fotosistemaa,
      };
    });
    })
    .catch(error => {
      // Manejar el error
      console.error(error);
    });
  },


  fetchalumnos() {
    // Realizar la solicitud para obtener la lista de alumnos actualizada
    axios.post('http://127.0.0.1:5050/alumnos')
    .then(response => {
      this.alumnos = response.data.map(alumno => {
      return {
            id_alumno:alumno.id_alumno,
            dni: alumno.dni,
            contrasena: alumno.contrasena,
            nombre: alumno.nombre,
            apellido: alumno.apellido,
            tipo_alumno: alumno.tipo_alumno,
            fotoSistema : alumno.fotoSistemaa,
      };
    });
    })
    .catch(error => {
      // Manejar el error
      console.error(error);
    });
  }


}
</script>