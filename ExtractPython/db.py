import psycopg2
from psycopg2 import OperationalError

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "9999"

def create_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Conexão com PostgreSQL estabelecida com sucesso!")
        return conn
    except OperationalError as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None

conn = create_connection()
if conn:
    conn.close()