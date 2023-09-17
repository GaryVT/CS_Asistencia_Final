#pip install psycopg2
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
import requests
import os
import json
import numpy as np
from flask_cors import CORS, cross_origin 
import re
import html

from backend.blueprints.funciones import transformarResultado, euclidianaDistance
from backend.blueprints.funciones import *

#from backend.models.mysql_user_model import UserModel
#model = UserModel()


from backend.models.postgres_usuario_model import UsuarioModel

model = UsuarioModel()


usuario_blueprint = Blueprint('usuario_blueprint', __name__)

#################################################

@usuario_blueprint.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        f = request.files['file']
        data = request.form.get('data')
        
        # si queremos guardar la foto
        filename = f.filename
        path = "C://Users//Usuario//Desktop//Ejemplo//proyecto_asistencias//Fotos//" + filename
        f.save(path)       
        # call openfaceAPI ##################################
        url = 'http://localhost:81/openfaceAPI'
        files = {'file': open(path, 'rb')}
        result = requests.post(url, files=files)
        result = result.json()      
        ##-----------------------------------------Coge vector2 = vector que genera a partir de la imagen
 
        vector = (result)
        vector = dictToString(vector)
        vector=toFloat(vector)
        ##------------------------------------------Coge vector1 == vector del sistema

        vector_db = model.obtener_foto(int(data))
        
        vector_db = dictToString(vector_db)
        vector_db=toFloat(vector_db)

        ##-----------------------------------------Hallando la distancia euclidiana

        vector = np.array(vector)

        vector_db = np.array(vector_db)

        Edistancia = np.linalg.norm(vector - vector_db)
        print(Edistancia)
        if Edistancia < 0.5 :
            #respuesta = ("Distancia Euclidiana: ", Edistancia," Si es la persona")
            respuesta = ("El usuario asistió")
        else:
            #respuesta = ("Distancia Euclidiana: ", Edistancia," No es la persona")
            respuesta = ("No es el usuario")
    #return jsonify(result)
    return jsonify(respuesta)


##################################################

@usuario_blueprint.route('/user', methods=['PUT'])
@cross_origin()
def crear_usuario():
    f = request.files['file']
    # si queremos guardar la foto
    filename = f.filename
    path = "C://Users//Usuario//Desktop//Ejemplo//proyecto_asistencias//Fotos//" + filename
    f.save(path)       
    # call openfaceAPI ##################################
    url = 'http://localhost:81/openfaceAPI'
    files = {'file': open(path, 'rb')}
    result = requests.post(url, files=files)
    json_response = json.loads(result.text)
    vector = json_response["result"]
    content = model.crear_usuario(request.form['dni']
                                , request.form['contrasena'], request.form['nombre']
                                , request.form['apellido'], request.form['tipousuario']
                                , vector)
    return jsonify(content)

@usuario_blueprint.route('/user', methods=['PATCH'])
@cross_origin()
def actualizar_usuario():
    f = request.files['file']
    # si queremos guardar la foto
    filename = f.filename
    path = "C://Users//Usuario//Desktop//Ejemplo//proyecto_asistencias//Fotos//" + filename
    f.save(path)       
    # call openfaceAPI ##################################
    url = 'http://localhost:81/openfaceAPI'
    files = {'file': open(path, 'rb')}
    result = requests.post(url, files=files)
    json_response = json.loads(result.text)
    vector = json_response["result"]
    content = model.actualizar_usuario(request.form['id_usuario']
                                       ,request.form['nombre']
                                       ,request.form['apellido']
                                       ,request.form['tipousuario']
                                       ,request.form['contrasena']
                                       ,request.form['dni']
                                       ,vector)   
    return jsonify(content)

@usuario_blueprint.route('/user', methods=['DELETE'])
@cross_origin()
def eliminar_usuario():
    return jsonify(model.eliminar_usuario(int(request.json['id_usuario'])))

@usuario_blueprint.route('/users', methods=['POST'])
@cross_origin()
def mostrar_usuarios():
    return jsonify(model.mostrar_usuarios())

@usuario_blueprint.route('/user/foto_sistema', methods=['POST'])
@cross_origin()
def obtener_foto():
     return jsonify(model.obtener_foto(int(request.json['id_usuario'])))



@usuario_blueprint.route('/userr', methods=['PUT'])
@cross_origin()
def crear_usuario_v2():
    content = model.crear_usuario_v2(request.json['dni']
                                       ,request.json['contrasena']
                                       ,request.json['nombre']
                                       ,request.json['apellido']
                                       ,request.json['tipousuario'])   


    return jsonify(content)