import sqlite3
DATA_BASE_NAME =  "data_base.db"
schema = "schema.sql"

#Global connection and cursor
connection = sqlite3.connect(DATA_BASE_NAME)
cursor = connection.cursor()

def execute_schema():  
    with open(schema) as file:
        print(file.read())
        connection.executescript(file.read())

def insert_data(table_name,columns_name,data):  # Insert data into data base

        insert_data_statement = (
            f'INSERT INTO {table_name}('
            f'{columns_name[1]}, {columns_name[2]}, {columns_name[3]})'
            'VALUES (?, ?, ?)'
        )

        cursor.executemany(insert_data_statement, data)
        connection.commit()
        connection.close()

def read_data(table_name):  # select all data from data base

        sql_statement = f'SELECT * FROM {table_name}'
        data = cursor.execute(sql_statement).fetchall()
        connection.close()

        return data


table_name = "actividades"
columns = ["id","nombre","fecha","lugar"]
data = [["Feria de las flores","carnaval en medellin","imagenes/Feriadelasflores.jpg"],["Evento 2","evento celebracion anual","imagenes/festivalinternacionaldeltango.jpg"]]
# insert_data(table_name,columns,data)

def print_data():
  sql_statement = "SELECT * FROM eventos"   
  for row in cursor.execute(sql_statement):
    print (row)


execute_schema()
#insert_data()

insert_data_statement = (
            f'INSERT INTO eventos('
            f'nombre, descripcion, img)'
            'VALUES (?, ?, ?)'
        )

cursor.executemany(insert_data_statement, data)
connection.commit()
print_data()

connection.close()