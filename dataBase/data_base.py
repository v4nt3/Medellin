import sqlite3
import json

DATA_BASE_NAME =  "data_base.db"
SCHEMA_FILE = "dataBase/schema.sql"

events_table = "EVENTOS"
events_columns = ["nombre","descripcion","imagen"]

activities_table = "ACTIVIDADES"
activities_columns = ["nombre","fecha","lugar","descripcion","imagen"]

places_table = "LUGARES"
places_columns = ["nombre","lugar","descripcion","imagen"]

#Global connection and cursor
connection = sqlite3.connect(DATA_BASE_NAME)
cursor = connection.cursor()

def execute_schema():  
    with open(SCHEMA_FILE) as file:
        cursor.executescript(file.read())


def insert_data(table_name,columns_name,data):  # Insert data into data base
        statment_columns = ""
        values = ""
        for i in range(len(columns_name)):
            statment_columns += columns_name[i]
            values += "?" 
            if (i+1) < len(columns_name):
                 statment_columns += ","
                 values += ","

        insert_data_statement = (
            f'INSERT INTO {table_name}('
            f'{statment_columns})'
            f'VALUES ({values})'
        )

        cursor.executemany(insert_data_statement, data)
        connection.commit()
        

def read_data(table_name,data_base_path):  # select all data from data base
        connection = sqlite3.connect(data_base_path)
        cursor = connection.cursor()
        sql_statement = f'SELECT * FROM {table_name}'
        data = cursor.execute(sql_statement).fetchall()
        connection.close()
        return data

def select_a_row(table_name,column_name,value) -> list:
        result = ""
        sql_statement = f'SELECT * FROM {table_name} WHERE {column_name} = {value}'
        row = cursor.execute(sql_statement)
        result = row.fetchall()
        
        if result:
            data = list(result[0])
            return data

        return ["Not Found"]

def print_data(table_name):
  sql_statement = f'SELECT * FROM {table_name}'
  for row in cursor.execute(sql_statement):
    print (row)

def read_json(json_name,columns_name):
    with open (json_name,"r") as json_file:
        json_list = json.load(json_file)

    data = []
    for json_data in json_list:
        aux = []
        for column in columns_name:
            aux.append(json_data[column])
        data.append(aux)

    return data

#create data base
#execute_schema()

#read the json file with the data from events,places and activities
events = read_json("dataBase/eventos.json",events_columns)
places = read_json("dataBase/lugares.json",places_columns)
activities = read_json("dataBase/actividades.json",activities_columns)

# insert data to the data base
#insert_data(events_table,events_columns,events)
# print_data(events_table)
# print("\n")

#insert_data(activities_table,activities_columns,activities)
# print_data(activities_table)
# print("\n")

#insert_data(places_table,places_columns,places)
# print_data(places_table)
# print("\n")

connection.close()