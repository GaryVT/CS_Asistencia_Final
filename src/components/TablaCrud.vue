<template>
      <div>



       <v-text-field
              v-model="search"
              append-icon="search"
              label="Search"
              single-line
              hdnie-details
            ></v-text-field>
      <v-data-table
        :headers="headers"
        :items="contacts"
        :search="search"
        :options.sync="pagination"
        hdnie-actions
        class="elevation-1"
        
      >
    
      <template slot="items" slot-scope="props">
  <td class="text-xs-right">{{ props.item.nombre }}</td>
  <td class="text-xs-right">{{ props.item.apellido }}</td>
  <td class="text-xs-right">{{ props.item.dni }}</td>
  <td class="text-xs-right">{{ props.item.tipousuario }}</td>
  <td class="text-xs-right">{{ props.item.contrasena }}</td>
  <td class="justify-center">
    <v-btn icon color="primary" @click="editItem(props.item)">
      <v-icon>mdi-pencil</v-icon>
    </v-btn>
    <v-btn icon color="error" @click="deleteItem(props.item)">
      <v-icon>mdi-delete</v-icon>
    </v-btn>
  </td>
</template>
   
    <template slot="no-data">
          <v-btn color="primary" @click="initialize"> Reset </v-btn>
    </template>
      </v-data-table>
  
       <div class="text-xs-center pt-2">
        <v-pagination v-model="pagination.page" :length="pages"></v-pagination>
      </div>
    </div>


  </template>
  
  <script>
    import axios from 'axios'
    export default {
      data: () => ({

         search: '',
         pagination:{rowsPerPage:10},
        dialog: false,

        headers: [
         
          { text: 'nombre', value: 'nombre' },
          { text: 'apellido', value: 'apellido' },
          { text: 'dni', value: 'dni' },
          { text: 'tipousuario', value: 'tipousuario' },
          { text: 'contrasena', value: 'contrasena' },
          { text: 'Actions', sortable: false}
        ],
        contacts: [],
        editedIndex: -1,
        editedItem: {
          nombre: '',
          apellido: '',
          dni: 0,
          tipousuario: 0,
          contrasena: ''
        },
        defaultItem: {
          nombre: '',
          apellido: '',
          dni: 0,
          tipousuario: 0,
          contrasena: ''
        }
      }),
  
      computed: {
        formTitle () {
          return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
        },
         pages () {
          if (this.pagination.rowsPerPage == null ||
            this.pagination.totalItems == null
          ) return 0
  
          return Math.ceil(this.pagination.totalItems / this.pagination.rowsPerPage)
        }
      },
  
      watch: {
        dialog (val) {
          val || this.close()
        }
      },
  
      created () {
        this.initialize()
      },
  
      methods: {
          fetchContacts(){ //
            axios.post('http://127.0.0.1:5050' + '/users').then((res) => {  
                    //console.log(res);
                    this.contacts = res.data; 
                    console.log("MOSTRANDO TABLA USUARIO");           
            })
            .catch((error) => {
                console.log(error)
            })
        },
        initialize(){
            this.fetchContacts();
        },
    editItem2() {
      // Lógica para editar el elemento
    },
    deleteUser(id) {
    axios.delete('http://127.0.0.1:5050/user', { data: { id_usuario: id } })
      .then(response => {
        // Realizar cualquier acción adicional después de borrar el usuario
        console.log(response.data);
        
      })
      .catch(error => {
        // Manejar el error
        console.error(error);
      });
    },
        
  
        editItem (item) {
          this.editedIndex = this.contacts.indexOf(item)
          this.editedItem = Object.assign({}, item)
          this.dialog = true
        },
  
        deleteItem (item) {
          console.log(item);
          
          const index = this.contacts.indexOf(item)
          const data = item.dni
          confirm('Are you sure you want to delete this item?') && this.contacts.splice(index, 1)
            console.log('deleted data');
  
            axios.delete('http://127.0.0.1:5050/user',{data})
            .then(response=>{
              console.log(response);
              
            })
  
        },
  
        close () {
          this.dialog = false
          setTimeout(() => {
            this.editedItem = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
          }, 300)
        },
  
        save () {
          if (this.editedIndex > -1) {
            console.log('edited data');
            console.log(this.editedItem);
            
  
            axios.put('/contact/'+this.editedItem.dni,{nombre:this.editedItem.nombre, apellido: this.editedItem.apellido})
            .then(response=>{
              console.log(response);
              
            })
  
            
            Object.assign(this.contacts[this.editedIndex], this.editedItem)
          } else {
            console.log('created data');
            console.log(this.editedItem);
  
             axios.post('/contact',{nombre:this.editedItem.nombre, apellido: this.editedItem.apellido})
            .then(response=>{
              console.log(response);
              
            })
  
            this.contacts.push(this.editedItem)
          }
          this.close()
        }
      }
    }
  </script>