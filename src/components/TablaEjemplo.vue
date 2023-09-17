<template>
    <v-simple-table>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">
              Name
            </th>
            <th class="text-left">
              Apellidos
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="item in items"
            :key="item.nombre"
          >
            <td>{{ item.nombre }}</td>
            <td>{{ item.apellido }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </template>
  
    <script>
    import axios from 'axios'
    export default{    
        data(){ 
            return { 
                items: [],
                newuser: {},
                postURL: 'http://127.0.0.1:5050'
                
            }
        },
        created(){ //
            axios.post(this.postURL + '/users').then((res) => {  
                    //console.log(res);
                    this.items = res.data; 
                    console.log("MOSTRANDO TABLA USUARIO");           
            })
            .catch((error) => {
                console.log(error)
            })
        }
    
    }
    </script>
    