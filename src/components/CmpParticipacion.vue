<template>
    <div>
      <v-data-table :items="participacions" :headers="columnas" item-key="part_id">
  
        <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>CRUD participaciones</v-toolbar-title>
          <v-divider class="mx-3" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="secondary" dark class="mb-2" v-bind="attrs" v-on="on">
                Nueva participacion
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">Crear participacion</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12">
                      <v-menu v-model="menu2" :close-on-content-click="false" :nudge-right="40"
                        transition="scale-transition" offset-y min-width="auto">
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field v-model="participacion.part_fecha" label="Fecha" prepend-icon="mdi-calendar"
                            readonly v-bind="attrs" v-on="on"></v-text-field>
                        </template>
                        <v-date-picker v-model="participacion.part_fecha" @input="menu2 = false"></v-date-picker>
                      </v-menu>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field v-model="participacion.cantidad" placeholder="Ingresa tu cantidad"
                        label="Cantidad"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field v-model="participacion.id_alumno" placeholder="ingresa el alumno"
                        label="alumno"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field v-model="participacion.id_curso" placeholder="ingresa el curso" label="curso">
                      </v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancelar</v-btn>
                <v-btn color="blue darken-1" text @click="createparticipacion">Crear</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>





          <!--DIALOG PARA EDITAR-->
          <v-dialog v-model="dialogEditarparticipacion" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">Editar participación</span>
        </v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols="12" sm="6" md="6">
              <v-menu v-model="menu2" :close-on-content-click="false" :nudge-right="40" transition="scale-transition" offset-y min-width="auto">
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field v-model="participacion.part_fecha" label="Fecha" prepend-icon="mdi-calendar" readonly v-bind="attrs" v-on="on"></v-text-field>
                </template>
                <v-date-picker v-model="participacion.part_fecha" @input="menu2 = false"></v-date-picker>
              </v-menu>
            </v-col>

            <v-col cols="12" sm="6" md="6">
              <v-text-field v-model="participacion.cantidad" label="Cantidad"></v-text-field>
            </v-col>

            <v-col cols="12" sm="6" md="6">
              <v-text-field v-model="participacion.id_alumno" label="ID Alumno"></v-text-field>
            </v-col>

            <v-col cols="12" sm="6" md="6">
              <v-text-field v-model="participacion.id_curso" label="ID Curso"></v-text-field>
            </v-col>

            <v-col cols="12" sm="6" md="6">
              <v-text-field v-model="participacion.part_id" label="ID Participación" readonly></v-text-field>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialogEditarparticipacion = false">Cancelar</v-btn>
          <v-btn color="blue darken-1" text @click="updateParticipacion">Actualizar</v-btn>
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
              @click="editarparticipacion(item)"
            >
              mdi-pencil
            </v-icon>
            <v-icon
              small
              @click="eliminarparticipacion(item)"
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
            dialogEditarparticipacion: false,
            U_participacions: [ { value: null, text: 'Seleccione una opción', disabled: true },
                          { value: '1', text: 'Administrador' },
                          { value: '2', text: 'participacion' },
                          { value: '3', text: 'participacion' },
                        ],
            participacions: [],
            selectedparticipacion: null,
            participacion: {
              part_id:'',
              part_fecha: '',
              cantidad: '',
              id_alumno: '',
              id_curso: ''
            },
            isDniReadOnly: true 
            
        };
    },
    methods:{
      close () {
        this.dialog = false
        
      },
      editarparticipacion(item) {
        this.participacion = { ...item };
        this.dialogEditarparticipacion = true;
      },
      
  
      createparticipacion() {
        const datos = {
            cantidad: this.participacion.cantidad,
            id_alumno: this.participacion.id_alumno,
            id_curso: this.participacion.id_curso,
            part_fecha: this.participacion.part_fecha
        };
          
  
          axios.put('http://127.0.0.1:5050/participacion', datos)
            .then(response => {
            // Aquí puedes manejar la respuesta del servidor
            console.log(response.data);
            // Cerrar el diálogo y actualizar la lista de usuarios si es necesario
            this.dialog = false;
            this.getUsuarios();
          })
          .catch(error => {
            // Manejar el error
            console.error(error);
            alert("No creado")
          });
      },
  
  
  
      updateParticipacion() {
      const payload = {
        cantidad: this.participacion.cantidad,
        id_alumno: this.participacion.id_alumno,
        id_curso: this.participacion.id_curso,
        part_fecha: this.participacion.part_fecha,
        part_id: this.participacion.part_id
      };
  
      axios.patch('http://127.0.0.1:5050/participacion', payload)
        .then(response => {
            console.log(response.data);
            // Cerrar el diálogo y actualizar la lista de usuarios si es necesario
            Object.assign(this.participacion, response.data);
        })
        .catch(error => {
          console.error('Error al actualizar la participación:', error);
        });
    },
  

  
      eliminarparticipacion(item) {
        // Realiza la lógica para eliminar el participacion
        // Puedes utilizar el ID del participacion o cualquier otra propiedad única para identificarlo
        // Por ejemplo, si tienes un ID único para cada participacion, podrías hacer algo como:
        const participacionId = item.part_id;
        
        // Luego, puedes hacer la llamada a la API para eliminar el participacion
        axios.delete('http://127.0.0.1:5050/participacion', { data: { part_id: participacionId } })
        .then(response => {
          // Realizar cualquier acción adicional después de borrar el participacion
          console.log(response.data);
          this.actualizarListaparticipacions(participacionId);
          
        })
        .catch(error => {
          // Manejar el error
          console.error(error);
        });
      },
      
      actualizarListaparticipacions(participacionId) {
        const index = this.participacions.findIndex(participacion => participacion.part_id === participacionId);
        if (index !== -1) {
          this.participacions.splice(index, 1);
        }
      },
      
    },
  
    computed: {
    participacionTitle () {
      return this.editedIndex === -1 ? 'Nuevo participacion' : 'Editar participacion'
    },
    columnas() {
        return [//izquierda solo es visual, derecha vale
            { text: 'CODIGO', value: 'part_id' },
            { text: 'Fecha', value: 'part_fecha' },
            { text: 'Cantidad', value: 'cantidad' },
            { text: 'Alumno', value: 'id_alumno' },
            { text: 'Curso', value: 'id_curso' },
            { text: 'Acciones', value: 'actions', sortable: false }
  
            ];
        }
    },
  
  
    created() {
    axios.post('http://127.0.0.1:5050/participaciones')
      .then(response => {
        this.participacions = response.data.map(participacion => {
        return {
              part_id:participacion.part_id,
              part_fecha:participacion.part_fecha,
              cantidad:participacion.cantidad,
              id_alumno:participacion.id_alumno,
              id_curso: participacion.id_curso,
         };

	


      });
      })
      .catch(error => {
        // Manejar el error
        console.error(error);
      });
    },
  
  
  }
  </script>