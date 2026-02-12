import psycopg2
import os
from psycopg2 import Error
from dotenv import load_dotenv
load_dotenv()
password = os.getenv("DB_PASSWORD")
def create_connection():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password=password,
            host="localhost",
            port="5432",
            database="loja_db"
        )
        return connection
    except Error as e:
        print(f"Erro com ao tentar conectar com o Banco de Dados: {e}")
        return None


def close_connection(connection):
    if connection:
        connection.close()
    print("Conexão com o Banco de Dados encerrada.")
    
