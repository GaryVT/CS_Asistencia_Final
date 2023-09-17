<template>
  <div>
    <v-data-table :items="usuarios" :headers="columnas" item-key="id_usuario">

      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>CRUD Usuarios</v-toolbar-title>
          <v-divider class="mx-3" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="secondary" dark class="mb-2" v-bind="attrs" v-on="on">
                Nuevo Usuario
              </v-btn>
            </template>

            <v-card>
              <v-card-title>
                <span class="text-h5">Crear Usuario</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field v-model="usuario.contrasena" type="password" placeholder="Ingresa tu contraseña" label="Contraseña"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field v-model="usuario.nombre" placeholder="Ingresa tu nombre" label="Nombre"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field v-model="usuario.apellido" placeholder="Ingresa tu apellido" label="Apellido"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-text-field v-model="usuario.dni" placeholder="Ingresa tu DNI" label="DNI"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-file-input v-model="usuario.file" accept="image/jpeg" label="Foto"></v-file-input>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                      <v-select v-model="usuario.tipousuario" :items="U_Usuarios" label="Tipo Usuario"></v-select>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Cancelar</v-btn>
                <v-btn color="blue darken-1" text @click="createUser">Crear</v-btn>
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
        <v-col cols="12" sm="6" md="6">
          <v-text-field v-model="usuario.apellido" placeholder="Ingresa tu apellido" label="Apellido"></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="6">
          <v-text-field v-model="usuario.contrasena" label="Contraseña" type="password" placeholder="Ingresa tu contraseña"></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="6">
          <v-text-field v-model="usuario.dni" label="Dni"></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="6">
          <v-file-input v-model="usuario.file" accept="image/jpeg" label="Foto"></v-file-input>
        </v-col>
        <v-col cols="12" sm="6" md="6">
          <v-text-field v-model="usuario.nombre" placeholder="Ingresa tu nombre" label="Nombre"></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="6">
          <v-text-field v-model="usuario.tipousuario" label="Tipo de usuario"></v-text-field>
        </v-col>
      </v-row>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="dialogEditarUsuario = false">Cancelar</v-btn>
      <v-btn color="blue darken-1" text @click="updateUser">Actualizar</v-btn>
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
            id_usuario:'',
            contrasena: '',
            nombre: '',
            apellido: '',
            dni: '',
            file: '',
            tipousuario:''
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
        usuarioData.append('contrasena', this.usuario.contrasena);
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
      const usuarioData = new FormData();
      usuarioData.append('id_usuario', this.usuario.id_usuario);
        usuarioData.append('dni', this.usuario.dni);
        usuarioData.append('contrasena', this.usuario.contrasena);
        usuarioData.append('nombre', this.usuario.nombre);
        usuarioData.append('apellido', this.usuario.apellido);
        usuarioData.append('tipousuario', this.usuario.tipousuario);
        usuarioData.append('file', this.usuario.file);
    // Realizar la solicitud al endpoint para actualizar el usuario
    axios.patch('http://127.0.0.1:5050/user', usuarioData)
    .then(response => {
      // La solicitud fue exitosa, realizar las acciones necesarias
      console.log('Usuario actualizado:', response.data);
      alert("Actualizado")

      // Aquí puedes realizar alguna acción adicional, como mostrar una notificación de éxito o recargar la lista de usuarios
      this.fetchUsuarios();
    })
    .catch(error => {
      // Hubo un error al realizar la solicitud, manejar el error
      console.error('Error al actualizar el usuario:', error);
      // Aquí puedes mostrar una notificación de error o realizar alguna acción de manejo de errores
    })
    .finally(() => {
      // Limpiar los campos del formulario o realizar acciones finales si es necesario
      this.dialogEditarUsuario = false; // Cerrar el diálogo después de actualizar

    });
  },

    eliminarUsuario(item) {
      // Realiza la lógica para eliminar el usuario
      // Puedes utilizar el ID del usuario o cualquier otra propiedad única para identificarlo
      // Por ejemplo, si tienes un ID único para cada usuario, podrías hacer algo como:
      const usuarioId = item.id_usuario;
      
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
      const index = this.usuarios.findIndex(usuario => usuario.id_usuario === usuarioId);
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
          { text: 'ID', value: 'id_usuario' },
          { text: 'contrasena', value: 'contrasena' },
          { text: 'Apellido', value: 'apellido' },
          { text: 'Nombre', value: 'nombre' },
          { text: 'file', value: 'fotoSistema' },
          { text: 'DNI', value: 'dni' },
          { text: 'tipousuario', value: 'tipousuario' },

          { text: 'Acciones', value: 'actions', sortable: false }

          ];
      }
  },


  created() {
  axios.post('http://127.0.0.1:5050/users')
    .then(response => {
      this.usuarios = response.data.map(usuario => {
      return {
            dni: usuario.dni,
            id_usuario:usuario.id_usuario,
            contrasena: usuario.contrasena,
            apellido: usuario.apellido,
            nombre: usuario.nombre,
            tipousuario: usuario.tipousuario,
            fotoSistema : usuario.fotoSistemaa,
      };
    });
    })
    .catch(error => {
      // Manejar el error
      console.error(error);
    });
  },


  fetchUsuarios() {
    // Realizar la solicitud para obtener la lista de usuarios actualizada
    axios.post('http://127.0.0.1:5050/users')
    .then(response => {
      this.usuarios = response.data.map(usuario => {
      return {
            dni: usuario.dni,
            id_usuario:usuario.id_usuario,
            contrasena: usuario.contrasena,
            apellido: usuario.apellido,
            nombre: usuario.nombre,
            tipousuario: usuario.tipousuario,
            fotoSistema : usuario.fotoSistemaa,
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