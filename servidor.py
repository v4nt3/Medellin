import os
import json
import sqlite3
from dataBase.data_base import read_data
# Obtiene la ruta absoluta al directorio actual de tu script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Luego, puedes usar esta ruta para acceder al archivo usuarios.txt
pedidos_file = os.path.join(current_dir, 'pedido.txt')
clientes_file = os.path.join(current_dir, 'cliente.txt')
usuarios_file = os.path.join(current_dir, 'usuarios.txt')

from flask import Flask, request, render_template, redirect, url_for, session,jsonify

data_base_path = "data_base.db"

app = Flask(__name__)

@app.route('/')
@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos_dos.html')

@app.route('/lugares')
def lugares():
    return render_template('lugares_dos.html')

@app.route('/prueba')
def prueba():
    data = read_data("data_base.db","actividades")
    return jsonify(data)

@app.route('/actividades')
def actividades():
    return render_template('actividades.html')

@app.route('/encuesta')
def encuesta():
    return render_template('encuesta.html')

@app.route('/obtenerActividades',methods=[ 'POST','GET'])
def obtenerActividades():
    pedido = ""
    if request.method == "GET":
        table_name = "ACTIVIDADES"
        data = read_data(table_name,data_base_path)
       
        return jsonify(data)
    return "Bad Request"

@app.route('/obtenerEventos',methods=[ 'POST','GET'])
def obtenerEventos():
    pedido = ""
    if request.method == "GET":
        table_name = "EVENTOS"
        data = read_data(table_name,data_base_path)
       
        return jsonify(data)
    return "Bad Request"

@app.route('/obtenerLugares',methods=[ 'POST','GET'])
def obtenerLugares():
    pedido = ""
    if request.method == "GET":
        table_name = "LUGARES"
        data = read_data(table_name,data_base_path)
       
        return jsonify(data)
    return "Bad Request"

if __name__ == '__main__':
   
    app.run(debug=True)