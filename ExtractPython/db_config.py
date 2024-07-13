import psycopg2
from psycopg2 import OperationalError

class connection_db:
    def __init__(self):
        self.DB_NAME = "project_development"
        self.DB_USER = "postgres"
        self.DB_PASSWORD = "postgres"
        self.DB_HOST = "localhost"
        self.DB_PORT = "9999"

    def create_connection(self):
        try:
            conn = psycopg2.connect(
                dbname=self.DB_NAME,
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                host=self.DB_HOST,
                port=self.DB_PORT
            )
            print("Conexão com PostgreSQL estabelecida com sucesso!")
            return conn
        except OperationalError as e:
            print(f"Erro ao conectar ao PostgreSQL: {e}")
            return None
