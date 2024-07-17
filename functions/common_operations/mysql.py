from mysql.connector import Error
import mysql.connector
import os
import json
import uuid

config = json.loads(open('config.json', 'r').read())

def run_mysql_command(command):
    connection = None
    cursor = None
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host=config['database']['host'],
            port=config['database']['port'],
            user=config['database']['user'],
            password=config['database']['password'],
            database=config['database']['name']
        )
        
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
    except Error as e:
        print(f"Error: {e}")
        return None
    

def select_mysql_command(command):
    connection = None
    cursor = None
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host=config['database']['host'],
            port=config['database']['port'],
            user=config['database']['user'],
            password=config['database']['password'],
            database=config['database']['name']
        )
        
        cursor = connection.cursor()
        cursor.execute(command)
        return cursor.fetchall()
    except Error as e:
        print(f"Error: {e}")


tabels = {
    'users': {
        'id': 'INT AUTO_INCREMENT PRIMARY KEY',
        'username': 'VARCHAR(255)',
        'password': 'VARCHAR(255)',
        'email': 'VARCHAR(255)',
        'created_at': 'DATETIME',
        'last_login': 'DATETIME'
    }
}

for table in tabels:
    run_mysql_command(f"CREATE TABLE IF NOT EXISTS `{table}` ({', '.join([f'{key} {value}' for key, value in tabels[table].items()])})")