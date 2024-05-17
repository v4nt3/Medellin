import os
import json
import sqlite3

# Obtiene la ruta absoluta al directorio actual de tu script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Luego, puedes usar esta ruta para acceder al archivo usuarios.txt
pedidos_file = os.path.join(current_dir, 'pedido.txt')
clientes_file = os.path.join(current_dir, 'cliente.txt')
usuarios_file = os.path.join(current_dir, 'usuarios.txt')

from flask import Flask, request, render_template, redirect, url_for, session,jsonify


def create_data_base(data_base_path,table_name,columns_name):
        connection = sqlite3.connect(data_base_path)
        cursor = connection.cursor()

        cursor.execute(f'DROP TABLE IF EXISTS {table_name}')

        create_table_statement = (
            f'CREATE TABLE {table_name} ('
            f'{columns_name[0]} INTEGER PRIMARY KEY,'
            f'{columns_name[1]} TEXT NOT NULL,'
            f'{columns_name[2]} TEXT NOT NULL,'
            f'{columns_name[3]} TEXT NOT NULL);'
        )
        cursor.execute(create_table_statement)

        connection.commit()
        connection.close()

def insert_data(data_base_path,table_name,columns_name,data):  # Insert data into data base
        connection = sqlite3.connect(data_base_path)
        cursor = connection.cursor()

        insert_data_statement = (
            f'INSERT INTO {table_name}('
            f'{columns_name[1]}, {columns_name[2]}, {columns_name[3]})'
            'VALUES (?, ?, ?)'
        )

        cursor.executemany(insert_data_statement, data)
        connection.commit()
        connection.close()

def read_data(data_base_path,table_name):  # select all data from data base

        connection = sqlite3.connect(data_base_path)
        cursor = connection.cursor()
        sql_statement = f'SELECT * FROM {table_name}'
        data = cursor.execute(sql_statement).fetchall()
        connection.close()

        return data

data_base_path = "data_base.db"
table_name = "actividades"
columns = ["id","nombre","fecha","lugar"]
data = [["1 Charla Concientizacion Cultural","Abril 9 2024 16:00","Universidad San Buenaventura"],["2 Charla Concientizacion Cultural","Abril 23 2024 16:00","Universidad San Buenaventura"]]
create_data_base("data_base.db","actividades",columns)
insert_data(data_base_path,table_name,columns,data)

app = Flask(__name__)

@app.route('/')
@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

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

@app.route('/obtenerActividades',methods=[ 'POST','GET'])
def obtenerActividades():
    pedido = ""
    if request.method == "GET":
        data = read_data(data_base_path,table_name)
       
        print(data)
        return jsonify(data)
    return "Bad Request"


if __name__ == '__main__':
   
    app.run(debug=True)