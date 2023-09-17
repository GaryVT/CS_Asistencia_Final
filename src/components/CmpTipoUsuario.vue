<template>
    <div>
      <v-data-table :items="usuarios" :headers="columnas" item-key="id">
  
        <template v-slot:top>
          <v-toolbar
            flat
          >
            <v-toolbar-title>CRUD Tipo Usuarios</v-toolbar-title>
            <v-divider
              class="mx-3"
              inset
              vertical
            ></v-divider>
            <v-spacer></v-spacer>
            
  
            
  
  
      <v-dialog
              v-model="dialog"
              max-width="500px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  color="secondary"
                  dark
                  class="mb-2"
                  v-bind="attrs"
                  v-on="on"
                >
                  Nuevo Tipo Usuario
                </v-btn>
              </template>
  
              <v-card>
                <v-card-title>
                  <span class="text-h5">Crear Tipo Usuario</span>
                </v-card-title>
    
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                        <v-text-field
                          v-model="tipousr_id"
                          type="password"
                          placeholder="Ingresa tu tipousr_id"
                          label="tipousr_id"
                        ></v-text-field>
                      </v-col>
                      <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                     
                        <v-text-field
                          v-model="nombre"
                          placeholder="Ingresa tu nombre"
                          label="Nombre"
                        ></v-text-field>
                      </v-col>
                      <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                        <v-text-field
                          v-model="apellido"
                          placeholder="Ingresa tu apellido"
                          label="Apellido"
                        ></v-text-field>
                      </v-col>
           
             
       
  
           
  
  
  
                      <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                        <v-text-field
                          v-model="nombre_tusr"
                          placeholder="Maximo 8 caracteres"
                          label="Dni"
                        ></v-text-field>
                      </v-col>
  
  
  
                      <v-col
                          cols="12"
                          sm="6"
                          md="6"
                        >
                          <v-file-input
  
                          v-model="file"
                          accept="image/jpg"
                          label="Foto"
                        ></v-file-input>
                        </v-col>
  
  
                      <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                      <v-container fluid>
                        <v-combobox
                          v-model="model"
                          :items="U_Usuarios"
                          hide-selected
                          hint="Se muestra maximo 5"
                          label="Tipo Usuario"
                          multiple
                          persistent-hint
                          small-chips
                        >
        
                        </v-combobox>
                       </v-container>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>
    
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="blue darken-1"
                    text
                    @click="close"
                  >
                    Cancelar
                  </v-btn>
                  <v-btn
                    color="blue darken-1"
                    text
                    @click="createUser"
                  >
                    Crear
                  </v-btn>
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
              @click="editarUsuario(item)"
            >
              mdi-pencil
            </v-icon>
            <v-icon
              small
              @click="eliminarUsuario(item)"
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
            dialogEditarUsuario: false,
            U_Usuarios: [ { value: null, text: 'Seleccione una opción', disabled: true },
                          { value: '1', text: 'Administrador' },
                          { value: '2', text: 'Alumno' },
                          { value: '3', text: 'Docente' },
                        ],
            usuarios: [],
            selectedUser: null,
            usuario: {
              id:'',
              tipousr_id: '',
              nombre: '',
              apellido: '',
              nombre_tusr: '',
              file: null
            },
            isDniReadOnly: true 
            
        };
    },
    methods:{
      close () {
        this.dialog = false
        
      },
  
      editarUsuario(item) {
        this.usuario = { ...item };
        this.dialogEditarUsuario = true;
      },
      
  
      createUser() {
        const usuarioData = new FormData();
          usuarioData.append('nombre_tusr', this.usuario.nombre_tusr);
          usuarioData.append('tipousr_id', this.usuario.tipousr_id);
          usuarioData.append('nombre', this.usuario.nombre);
          usuarioData.append('apellido', this.usuario.apellido);
          usuarioData.append('tipousuario', this.usuario.tipousuario);
          usuarioData.append('file', this.usuario.file);
  
          axios.put('http://127.0.0.1:5050/user', usuarioData)
            .then(response => {
            // Aquí puedes manejar la respuesta del servidor
            console.log(response.data);
            // Cerrar el diálogo y actualizar la lista de usuarios si es necesario
            this.dialog = false;
            alert("Usuario Creado")
          })
          .catch(error => {
            // Manejar el error
            console.error(error);
          });
      },
  
  
  
      
      updateUser() {
      const usuarioData = new usuarioData();
        usuarioData.append('id_usuario', this.usuario.id);
        usuarioData.append('tipousr_id', this.usuario.tipousr_id);
        usuarioData.append('password', this.usuario.password);
        usuarioData.append('nombre', this.usuario.nombre);
        usuarioData.append('apellido', this.usuario.apellido);
        usuarioData.append('edad', this.usuario.edad);
        usuarioData.append('genero', this.usuario.genero);
        usuarioData.append('correo_electronico', this.usuario.correo);
        usuarioData.append('telefono', this.usuario.telefono);
        usuarioData.append('direccion', this.usuario.direccion);
        usuarioData.append('nombre_tusr', this.usuario.nombre_tusr);
        usuarioData.append('file', this.usuario.file);
  
        axios
          .patch('http://127.0.0.1:5050/user', usuarioData)
          .then(response => {
            // Aquí puedes manejar la respuesta del servidor
            console.log(response.data);
            // Cerrar el diálogo y actualizar la lista de usuarios si es necesario
            Object.assign(this.usuario, response.data);
  
          })
          .catch(error => {
            // Manejar el error
            console.error(error);
          });
      },
  
      eliminarUsuario(item) {
        // Realiza la lógica para eliminar el usuario
        // Puedes utilizar el ID del usuario o cualquier otra propiedad única para identificarlo
        // Por ejemplo, si tienes un ID único para cada usuario, podrías hacer algo como:
        const usuarioId = item.id;
        
        // Luego, puedes hacer la llamada a la API para eliminar el usuario
        axios.delete('http://127.0.0.1:5050/user', { data: { id_usuario: usuarioId } })
        .then(response => {
          // Realizar cualquier acción adicional después de borrar el usuario
          console.log(response.data);
          this.actualizarListaUsuarios(usuarioId);
          
        })
        .catch(error => {
          // Manejar el error
          console.error(error);
        });
      },
      
      actualizarListaUsuarios(usuarioId) {
        const index = this.usuarios.findIndex(usuario => usuario.id === usuarioId);
        if (index !== -1) {
          this.usuarios.splice(index, 1);
        }
      },
      
    },
  
    computed: {
    usuarioTitle () {
      return this.editedIndex === -1 ? 'Nuevo Usuario' : 'Editar Usuario'
    },
    columnas() {
        return [
            { text: 'Codigo', value: 'tipousr_id' },
            { text: 'Nombre', value: 'nombre_tusr' },
            { text: 'Acciones', value: 'actions', sortable: false }
  
            ];
        }
    },
  
  
    created() {
    axios.post('http://127.0.0.1:5050/tipo_usuarios')
      .then(response => {
        this.usuarios = response.data.map(user => {
        return {
          nombre_tusr : user.nombre_tusr,
              tipousr_id: user.tipousr_id,
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