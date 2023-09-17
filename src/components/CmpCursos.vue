<template>
    <div>
      <v-data-table :items="usuarios" :headers="columnas" item-key="id">
  
        <template v-slot:top>
          <v-toolbar
            flat
          >
            <v-toolbar-title>CRUD Cursos</v-toolbar-title>
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
                  Nuevo Usuario
                </v-btn>
              </template>
  
              <v-card>
                <v-card-title>
                  <span class="text-h5">Crear Curso</span>
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
                          v-model="nombre_curso"
                          type="password"
                          placeholder="Ingresa tu nombre_curso"
                          label="nombre_curso"
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
                          v-model="descripcion"
                          placeholder="Ingresa tu descripcion"
                          label="descripcion"
                        ></v-text-field>
                      </v-col>
           
                      <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                        <v-text-field
                          v-model="dni"
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
            
            <v-dialog v-model="dialogEditarUsuario" max-width="500px">
              <v-card>
                <v-card-title>
                  <span class="headline">Editar Usuario</span>
                </v-card-title>
                <v-card-text>
                  <v-row>
                    <v-col
                      cols="12"
                      sm="6"
                      md="6"
                    >
                      <v-text-field
                        v-model="usuario.nickname"
                        placeholder="Ingresa tu nickname"
                        label="Nickname"
                      ></v-text-field>
                    </v-col>
                    <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                        <v-text-field

                          v-model="usuario.password"
                          label="Password"
                          type="password"
                          placeholder="Ingresa tu contraseña"
                        ></v-text-field>
                      </v-col>
                      <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                        <v-text-field
                          v-model="usuario.nombre"
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
                          v-model="usuario.apellido"
                          placeholder="Ingresa tu apellido"
                          label="Apellido"
                        ></v-text-field>
                      </v-col>
                      <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                        <v-select
                        v-model="usuario.genero"
                        :items="generoOptions"
                        label="Género"
                      ></v-select>
                      </v-col>
                      <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                          <v-text-field
                          v-model="usuario.correo"
                          label="Correo Electrónico"
                          type="email"
                          placeholder="ejemplo@dominio.com"

                        ></v-text-field>
                      </v-col>

                      <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                        <v-text-field
                          v-model="usuario.telefono"
                          label="Telefono"
                        ></v-text-field>
                      </v-col>
                      <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                        <v-text-field
                          v-model="usuario.direccion"
                          label="Direccion"
                        ></v-text-field>
                      </v-col>
                      <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                        <v-text-field
                          v-model="usuario.dni"
                          label="Dni"
                          :readonly="isDniReadOnly"
                        ></v-text-field>
                      </v-col>
                      <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                        <v-text-field
                          v-model="usuario.edad"
                          label="Edad"
                        ></v-text-field>
                      </v-col>
                      <v-col
                        cols="12"
                        sm="6"
                        md="6"
                      >
                        <v-file-input

                        v-model="usuario.foto"
                        accept="image/png"
                        label="Foto"
                      ></v-file-input>
                      </v-col>
                  </v-row>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="blue darken-1"
                    text
                    @click="dialogEditarUsuario = false"
                  >
                    Cancelar
                  </v-btn>
                  <v-btn
                    color="blue darken-1"
                    text
                    @click="updateUser"
                  >
                    Actualizar
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
              style="submit"
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
              nombre_curso: '',
              nombre: '',
              descripcion: '',
              dni: '',
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
          usuarioData.append('dni', this.usuario.dni);
          usuarioData.append('nombre_curso', this.usuario.nombre_curso);
          usuarioData.append('nombre', this.usuario.nombre);
          usuarioData.append('descripcion', this.usuario.descripcion);
          usuarioData.append('id_docente', this.usuario.id_docente);
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
        usuarioData.append('id_curso', this.usuario.id);
        usuarioData.append('nombre_curso', this.usuario.nombre_curso);
        usuarioData.append('password', this.usuario.password);
        usuarioData.append('nombre', this.usuario.nombre);
        usuarioData.append('descripcion', this.usuario.descripcion);
        usuarioData.append('edad', this.usuario.edad);
        usuarioData.append('genero', this.usuario.genero);
        usuarioData.append('correo_electronico', this.usuario.correo);
        usuarioData.append('telefono', this.usuario.telefono);
        usuarioData.append('direccion', this.usuario.direccion);
        usuarioData.append('dni', this.usuario.dni);
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
        axios.delete('http://127.0.0.1:5050/curso', { data: { id_curso: usuarioId } })
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
            { text: 'ID', value: 'id' },
            { text: 'nombre_curso', value: 'nombre_curso' },
            { text: 'descripcion', value: 'descripcion' },
            { text: 'id_docente', value: 'id_docente' },
            { text: 'Acciones', value: 'actions', sortable: false }
  
            ];
        }
    },
  
  
    created() {
    axios.post('http://127.0.0.1:5050/cursos')
      .then(response => {
        this.usuarios = response.data.map(user => {
        return {
          dni : user.dni,
          id:user.id_curso,
              nombre_curso: user.nombre_curso,
              descripcion: user.descripcion,
              id_docente: user.id_docente,
              file : user.file,
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