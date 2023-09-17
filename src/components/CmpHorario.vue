<template>
  <div>
    <v-data-table :items="horarios" :headers="columnas" item-key="id_horario">

      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>CRUD Horario</v-toolbar-title>
          <v-divider class="mx-3" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="secondary" dark class="mb-2" v-bind="attrs" v-on="on">
                Nuevo Horario
              </v-btn>
            </template>

<v-card>
  <v-card-title>
    <span class="headline">Editar Horario</span>
  </v-card-title>

  <v-card-text>
    <v-text-field v-model="horario.id_curso" type="text" placeholder="Ingresa el ID del curso" label="ID del Curso"></v-text-field>
    <v-menu v-model="timePickerOpen" :close-on-content-click="false" transition="scale-transition" offset-y min-width="290px">
      <template v-slot:activator="{ on }">
        <v-text-field v-model="horario.hora_inicio" v-on="on" label="Hora de inicio" readonly></v-text-field>
      </template>
      <v-time-picker v-model="horario.hora_inicio" horarioat="HH:mm"></v-time-picker>
    </v-menu>
    <v-menu v-model="timePickerOpen" :close-on-content-click="false" transition="scale-transition" offset-y min-width="290px">
      <template v-slot:activator="{ on }">
        <v-text-field v-model="horario.hora_fin" v-on="on" label="Hora de fin" readonly></v-text-field>
      </template>
      <v-time-picker v-model="horario.hora_fin" horarioat="HH:mm"></v-time-picker>
    </v-menu>
    <v-text-field v-model="horario.dia" type="text" placeholder="Ingresa el día" label="Día"></v-text-field>
    <v-text-field v-model="horario.aula" type="text" placeholder="Ingresa el aula" label="Aula"></v-text-field>
  </v-card-text>

  <v-card-actions>
    <v-spacer></v-spacer>
    <v-btn color="blue darken-1" text @click="close">Cancelar</v-btn>
    <v-btn color="blue darken-1" text @click="createHorario">Crear</v-btn>
  </v-card-actions>
</v-card>
</v-dialog>



<v-dialog v-model="dialogEditarhorario" max-width="500px">
            <v-card>
              <v-card-title>
                <span class="text-h5">Editar Horario</span>
              </v-card-title>

              <v-card-text>
              <v-text-field v-model="horario.id_curso" placeholder="Ingresa el ID del curso" label="ID del Curso"></v-text-field>

              <v-menu v-model="timePickerOpen" :close-on-content-click="false" transition="scale-transition" offset-y min-width="290px">
                <template v-slot:activator="{ on }">
                  <v-text-field v-model="horario.hora_inicio" v-on="on" label="Hora de inicio" readonly></v-text-field>
                </template>
                <v-time-picker v-model="horario.hora_inicio" horarioat="HH:mm"></v-time-picker>
              </v-menu>

              <v-menu v-model="timePickerOpen" :close-on-content-click="false" transition="scale-transition" offset-y min-width="290px">
                <template v-slot:activator="{ on }">
                  <v-text-field v-model="horario.hora_fin" v-on="on" label="Hora de fin" readonly></v-text-field>
                </template>
                <v-time-picker v-model="horario.hora_fin" horarioat="HH:mm"></v-time-picker>
              </v-menu>

              <v-text-field v-model="horario.dia" type="text" placeholder="Ingresa el día" label="Día"></v-text-field>
              
              <v-text-field v-model="horario.aula" type="text" placeholder="Ingresa el aula" label="Aula"></v-text-field>
            </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="dialogEditarhorario = false">Cancelar</v-btn>
                <v-btn color="blue darken-1" text @click="updateHorario">Actualizar</v-btn>
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
            @click="editarhorario(item)"
            
          >
            mdi-pencil
          </v-icon>
          <v-icon
            small
            @click="eliminarhorario(item)"
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
          dialogEditarhorario: false,
          U_horarios: [ { value: null, text: 'Seleccione una opción', disabled: true },
                        { value: '1', text: 'Administrador' },
                        { value: '2', text: 'Alumno' },
                        { value: '3', text: 'Docente' },
                      ],
          horarios: [],
          selectedhorario: null,
          horario: {
            id_curso: "",
            hora_inicio: '',
            hora_fin: '',
            dia: '',
            aula: '',

          },
          isDniReadOnly: true,
          time: null,
          menu2: false,
          modal2: false,
          
      };
  },
  methods:{
    close () {
      this.dialog = false
      
    },

    editarhorario(item) {
      this.horario = { ...item };
      this.dialogEditarhorario = true;
    },
    

    createHorario() {
    const horarioData = {
      id_curso: this.horario.id_curso,
      hora_inicio: this.horario.hora_inicio,
      hora_fin: this.horario.hora_fin,
      dia: this.horario.dia,
      aula: this.horario.aula
    };

    axios
      .put('http://127.0.0.1:5050/horario', horarioData)
      .then(response => {
        // Aquí puedes manejar la respuesta del servidor
        console.log(response.data);
        // Cerrar el diálogo y actualizar la lista de horarios si es necesario
        this.dialog = false;
        alert("Horario creado");
        this.fetchHorarios();
      })
      .catch(error => {
        // Manejar el error
        console.error(error);
      });
  },
  horarioatTime(time) {
  // Asegurarse de que el tiempo sea una instancia de Date
  if (!(time instanceof Date)) {
    time = new Date(time);
  }
  // horarioatear el tiempo como HH:mm
  const hours = String(time.getHours()).padStart(2, '0');
  const minutes = String(time.getMinutes()).padStart(2, '0');
  return `${hours}:${minutes}`;
},



updateHorario() {
  const horarioData = {
    id_horario: this.horario.id_horario,
    id_curso: this.horario.id_curso,
    hora_inicio: this.horario.hora_inicio,
    hora_fin: this.horario.hora_fin,
    dia: this.horario.dia,
    aula: this.horario.aula
  };

  axios
    .patch('http://127.0.0.1:5050/horario', horarioData)
    .then(response => {
      console.log(response.data);
      this.dialogEditarhorario = false;
      alert("Horario actualizado");
      this.fetchHorarios();
    })
    .catch(error => {
      console.error(error);
    });
},



    eliminarhorario(item) {
      // Realiza la lógica para eliminar el horario
      // Puedes utilizar el ID del horario o cualquier otra propiedad única para identificarlo
      // Por ejemplo, si tienes un ID único para cada horario, podrías hacer algo como:
      const horarioId = item.id_horario;
      
      // Luego, puedes hacer la llamada a la API para eliminar el horario
      axios.delete('http://127.0.0.1:5050/horario', { data: { id_horario: horarioId } })
      .then(response => {
        // Realizar cualquier acción adicional después de borrar el horario
        console.log(response.data);
        this.actualizarListahorarios(horarioId);
        
      })
      .catch(error => {
        // Manejar el error
        console.error(error);
      });
    },
    actualizarListahorarios(horarioId) {
    const index = this.horarios.findIndex(horario => horario.id_horario === horarioId);
    if (index !== -1) {
      this.horarios.splice(index, 1);
    }
  },
    
   
    
  },

  computed: {
  horarioTitle () {
    return this.editedIndex === -1 ? 'Nuevo horario' : 'Editar horario'
  },
  columnas() {
      return [
          { text: 'ID', value: 'id_horario' },
          { text: 'id_curso', value: 'id_curso' },
          { text: 'hora_inicio', value: 'hora_inicio' },
          { text: 'hora_fin', value: 'hora_fin' },
          { text: 'dia', value: 'dia' },
          { text: 'aula', value: 'aula' },
          { text: 'Acciones', value: 'actions', sortable: false }

          ];
      }
  },


  created() {
  axios.post('http://127.0.0.1:5050/horarios')
    .then(response => {
      this.horarios = response.data.map(horario => {
      return {
            id_horario:horario.id_horario,
            id_curso:horario.id_curso,
            hora_inicio: horario.hora_inicio,
            hora_fin: horario.hora_fin,
            dia: horario.dia,
            aula: horario.aula,
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
