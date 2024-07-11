from sqlalchemy import create_engine
import psycopg2
from db_config import connection_db

class Process:
    def __init__(self, deputy, proposition):
        self.deputy = deputy
        self.proposition = proposition
        db = connection_db()
        self.conn = db.create_connection()
        self.engine = create_engine(f'postgresql://{db.DB_USER}:{db.DB_PASSWORD}@{db.DB_HOST}:{db.DB_PORT}/{db.DB_NAME}')

    def insert_deputies(self, deputies_df):
        cursor = self.conn.cursor()

        try:
            # Print para debug: verificar as colunas presentes no DataFrame
            print("Colunas do DataFrame de deputados:")
            print(deputies_df.columns)

            for index, row in deputies_df.iterrows():
                sql = """
                      INSERT INTO deputies(id, civil_name, party_initials)
                      VALUES (%s, %s, %s)
                  """
                cursor.execute(sql, (row['id'], row['civil_name'], row['party_initials']))
                # Verifica quantas linhas foram afetadas pela inserção
                print(f"Inseridas {cursor.rowcount} linha(s) para deputado {row['civil_name']}")
            self.conn.commit()
            print("Dados dos deputados inseridos com sucesso!")

        except Exception as e:
            print(f"Erro ao inserir dados dos deputados: {str(e)}")

        finally:
            cursor.close()

    # def insert_propositions(self, propositions_df):
    #     cursor = self.conn.cursor()
    #
    #     try:
    #
    #         for index, row in propositions_df.iterrows():
    #             sql = """
    #                       INSERT INTO proposition(id, civil_name, party_initials)
    #                       VALUES (%s, %s, %s)
    #                   """
    #             cursor.execute(sql, (row['id'], row['civil_name'], row['party_initials']))
    #
    #         self.conn.commit()
    #         print("Dados dos deputados inseridos com sucesso!")
    #
    #     except Exception as e:
    #         print(f"Erro ao inserir dados dos deputados: {str(e)}")
    #
    #     cursor.close()
    #
    # def insert_themes(self, themes_df):
    #     cursor = self.conn.cursor()
    #
    #     try:
    #         cursor = self.conn.cursor()
    #
    #         for index, row in themes_df.iterrows():
    #             sql = """
    #                       INSERT INTO deputies(id, name, party_initials)
    #                       VALUES (%s, %s, %s)
    #                   """
    #             cursor.execute(sql, (row['id'], row['name'], row['party_initials']))
    #
    #         self.conn.commit()
    #         print("Dados dos deputados inseridos com sucesso!")
    #
    #     except Exception as e:
    #         print(f"Erro ao inserir dados dos deputados: {str(e)}")
    #
    #     cursor.close()
    # def insert_votes(self, votes_df):
    #     cursor = self.conn.cursor()
    #
    #     try:
    #         cursor = self.conn.cursor()
    #
    #         for index, row in votes_df.iterrows():
    #             sql = """
    #                       INSERT INTO deputies(id, name, party_initials)
    #                       VALUES (%s, %s, %s)
    #                   """
    #             cursor.execute(sql, (row['id'], row['name'], row['party_initials']))
    #
    #         self.conn.commit()
    #         print("Dados dos deputados inseridos com sucesso!")
    #
    #     except Exception as e:
    #         print(f"Erro ao inserir dados dos deputados: {str(e)}")
    #
    #     cursor.close()
