from db_config import connection_db

class Process:
    def __init__(self, deputy, proposition):
        self.deputy = deputy
        self.proposition = proposition
        db = connection_db()
        self.conn = db.create_connection()

    def insert_deputies(self, deputies_df):
        if self.conn:
            try:
                with self.conn.cursor() as cursor:
                    print(deputies_df.columns)

                    for index, row in deputies_df.iterrows():
                        cursor.execute("SELECT id FROM deputies WHERE id = %s", (row['id'],))
                        existing_deputy = cursor.fetchone()

                        if existing_deputy:
                            sql = """
                                  UPDATE deputies
                                  SET civil_name = %s, party_initials = %s, updated_at = CURRENT_TIMESTAMP
                                  WHERE id = %s
                                  """
                            cursor.execute(sql, (row['civil_name'], row['party_initials'], row['id']))
                        else:
                            sql = """
                                  INSERT INTO deputies(id, civil_name, party_initials, created_at, updated_at)
                                  VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                                  """
                            cursor.execute(sql, (row['id'], row['civil_name'], row['party_initials']))

                        if isinstance(row['proposition_ids'], list):
                            for proposition_id in row['proposition_ids']:
                                cursor.execute(
                                    "SELECT * FROM deputies_propositions WHERE deputy_id = %s AND proposition_id = %s",
                                    (row['id'], proposition_id))
                                association_exists = cursor.fetchone()
                                if not association_exists:
                                    cursor.execute(
                                        "INSERT INTO deputies_propositions(deputy_id, proposition_id, created_at, updated_at) VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                                        (row['id'], proposition_id))

                self.conn.commit()
                print("Dados dos deputados e associações inseridos/atualizados com sucesso!")

            except Exception as e:
                print(f"Erro ao inserir/atualizar dados dos deputados: {str(e)}")
                self.conn.rollback()
    def insert_propositions(self, propositions_df):
        if self.conn:
            try:
                with self.conn.cursor() as cursor:
                    print(propositions_df.columns)

                    for index, row in propositions_df.iterrows():
                        cursor.execute("SELECT id FROM propositions WHERE id = %s", (row['id'],))
                        existing_proposition = cursor.fetchone()

                        if existing_proposition:
                            sql = """
                                  UPDATE propositions
                                  SET proposition_type = %s, summary = %s, updated_at = CURRENT_TIMESTAMP
                                  WHERE id = %s
                                  """
                            cursor.execute(sql, (row['proposition_type'], row['summary'], row['id']))
                        else:
                            sql = """
                                  INSERT INTO propositions(id, proposition_type, summary, created_at, updated_at)
                                  VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                                  """
                            cursor.execute(sql, (row['id'], row['proposition_type'], row['summary']))

                    self.conn.commit()
                    print("Dados das proposições inseridos/atualizados com sucesso!")

            except Exception as e:
                print(f"Erro ao inserir/atualizar dados das proposições: {str(e)}")
                self.conn.rollback()

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Conexão com PostgreSQL fechada.")