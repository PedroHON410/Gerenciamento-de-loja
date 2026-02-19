import psycopg2
import os
from psycopg2 import Error
from dotenv import load_dotenv
load_dotenv()
def create_connection():
    try:
        connection = psycopg2.connect(
            user=os.getenv('DB_USER') ,
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME')
        )
        return connection
    except Error as e:
        print(f"Erro com ao tentar conectar com o Banco de Dados: {e}")
        return None


def close_connection(connection):
    if connection:
        connection.close()    
