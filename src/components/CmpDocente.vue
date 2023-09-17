<template>
  <div>
    <v-data-table :items="docentes" :headers="columnas" item-key="id_docente">

      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>CRUD docentes</v-toolbar-title>
          <v-divider class="mx-3" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="secondary" dark class="mb-2" v-bind="attrs" v-on="on">
                Nuevo docente
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">Crear docente</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field v-model="docente.id_usuario" placeholder="Ingresa ID Usuario" label="ID Usuario"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field v-model="docente.tipousr_id" placeholder="Ingresa Tipo Usuario" label="Tipo Usuario"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field v-model="docente.tipo_docente" placeholder="Ingresa Tipo Docente" label="Tipo Docente"></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancelar</v-btn>
                <v-btn color="blue darken-1" text @click="createDocente">Crear</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          

          

          <v-dialog v-model="dialogEditardocente" max-width="500px">
  <v-card>
    <v-card-title>
      <span class="headline">Editar docente</span>
    </v-card-title>
    <v-card-text>
      <v-row>
        <v-col cols="12" sm="6" md="6">
        <v-text-field v-model="docente.id_usuario" placeholder="Ingresa ID Usuario" label="ID Usuario"></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="6">
        <v-text-field v-model="docente.tipousr_id" placeholder="Ingresa Tipo Usuario" label="Tipo Usuario"></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="6">
        <v-text-field v-model="docente.tipo_docente" placeholder="Ingresa Tipo Docente" label="Tipo Docente"></v-text-field>
        </v-col>
      </v-row>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="dialogEditardocente = false">Cancelar</v-btn>
      <v-btn color="blue darken-1" text @click="updateDocente">Actualizar</v-btn>
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
            @click="editardocente(item)"
          >
            mdi-pencil
          </v-icon>
          <v-icon
            small
            @click="eliminardocente(item)"
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
          dialogEditardocente: false,
          U_docentes: [ { value: null, text: 'Seleccione una opción', disabled: true },
                        { value: '1', text: 'Administrador' },
                        { value: '2', text: 'Alumno' },
                        { value: '3', text: 'Docente' },
                      ],
          docentes: [],
          selectedUser: null,
          docente: {
            id_docente:'',
            contrasena: '',
            nombre: '',
            apellido: '',
            dni: '',
            file: '',
            tipodocente:'',
            id_usuario:'',
            tipousr_id:'',
            tipo_docente:''
          },
          isDniReadOnly: true 
          
      };
  },
  methods:{
    close () {
      this.dialog = false
      
    },

    editardocente(item) {
      this.docente = { ...item };
      this.dialogEditardocente = true;
    },
    

    createDocente() {
      const docenteData = {
        id_usuario: this.docente.id_usuario,
        tipo_docente: this.docente.tipo_docente,
        tipousr_id: this.docente.tipousr_id
      };

        axios.put('http://127.0.0.1:5050/docente', docenteData)
          .then(response => {
          // Aquí puedes manejar la respuesta del servidor
          console.log(response.data);
          // Cerrar el diálogo y actualizar la lista de docentes si es necesario
          this.dialog = false;
          alert("docente Creado")
        })
        .catch(error => {
          // Manejar el error
          console.error(error);
        });
    },



    
    updateDocente() {
    // Construir el objeto FormData con los datos del docente
    const docenteData = {
        id_docente: this.docente.id_docente,
        id_usuario: this.docente.id_usuario,
        tipo_docente: this.docente.tipo_docente,
        tipousr_id: this.docente.tipousr_id
      };

    // Realizar la solicitud al endpoint para actualizar el docente
    axios.patch('http://127.0.0.1:5050/docente', docenteData)
      .then(response => {
        // La solicitud fue exitosa, realizar las acciones necesarias
        console.log('Docente actualizado:', response.data);
        alert("Docente Actualizado")

        // Aquí puedes realizar alguna acción adicional, como mostrar una notificación de éxito o recargar la lista de docentes
        this.fetchDocentes();

        // Cerrar el diálogo de edición
        this.dialogEditardocente = false;
      })
      .catch(error => {
        // Hubo un error al realizar la solicitud, manejar el error
        console.error('Error al actualizar el docente:', error);
        // Aquí puedes mostrar una notificación de error o realizar alguna acción de manejo de errores
      });
  },

    eliminardocente(item) {
      // Realiza la lógica para eliminar el docente
      // Puedes utilizar el ID del docente o cualquier otra propiedad única para identificarlo
      // Por ejemplo, si tienes un ID único para cada docente, podrías hacer algo como:
      const docenteId = item.id_docente;
      
      // Luego, puedes hacer la llamada a la API para eliminar el docente
      axios.delete('http://127.0.0.1:5050/docente', { data: { id_docente: docenteId } })
      .then(response => {
        // Realizar cualquier acción adicional después de borrar el docente
        console.log(response.data);
        this.actualizarListadocentes(docenteId);
        
      })
      .catch(error => {
        // Manejar el error
        console.error(error);
      });
    },
    
    actualizarListadocentes(docenteId) {
      const index = this.docentes.findIndex(docente => docente.id_docente === docenteId);
      if (index !== -1) {
        this.docentes.splice(index, 1);
      }
    },
    
  },

  computed: {
  docenteTitle () {
    return this.editedIndex === -1 ? 'Nuevo docente' : 'Editar docente'
  },
  columnas() {
      return [
          { text: 'COD', value: 'id_docente' },
          { text: 'DNI', value: 'dni' },
          { text: 'contrasena', value: 'contrasena' },
          { text: 'Apellido', value: 'apellido' },
          { text: 'Nombre', value: 'nombre' },
          { text: 'file', value: 'fotoSistema' },
          { text: 'tipo_docente', value: 'tipo_docente' },
          { text: 'Acciones', value: 'actions', sortable: false }

          ];
      }
  },


  created() {
  axios.post('http://127.0.0.1:5050/docentes')
    .then(response => {
      this.docentes = response.data.map(docente => {
      return {
            id_docente:docente.id_docente,
            dni: docente.dni,
            contrasena: docente.contrasena,
            nombre: docente.nombre,
            apellido: docente.apellido,
            tipo_docente: docente.tipo_docente,
            fotoSistema : docente.fotoSistemaa,

            id_usuario : docente.id_usuario,
            tipousr_id : docente.tipousr_id,

      };
    });
    })
    .catch(error => {
      // Manejar el error
      console.error(error);
    });
  },


  fetchdocentes() {
    // Realizar la solicitud para obtener la lista de docentes actualizada
    axios.post('http://127.0.0.1:5050/docentes')
    .then(response => {
      this.docentes = response.data.map(docente => {
      return {
            id_docente:docente.id_docente,
            dni: docente.dni,
            contrasena: docente.contrasena,
            nombre: docente.nombre,
            apellido: docente.apellido,
            tipo_docente: docente.tipo_docente,
            fotoSistema : docente.fotoSistemaa,
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