from db_config import connection_db

class Process:
    def __init__(self, deputy, proposition):
        self.deputy = deputy
        self.proposition = proposition
        db = connection_db()
        self.conn = db.create_connection()

    def insert_deputies(self, deputies_df):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                print(deputies_df.columns)

                for index, row in deputies_df.iterrows():
                    cursor.execute("SELECT id FROM deputies WHERE id = %s", (row['id'],))
                    existing_deputy = cursor.fetchone()

                    if existing_deputy:
                        sql = """
                              UPDATE deputies
                              SET civil_name = %s, party_initials = %s, proposition_id = %s, updated_at = CURRENT_TIMESTAMP
                              WHERE id = %s
                              """
                        cursor.execute(sql, (row['civil_name'], row['party_initials'], row['proposition_ids'],  row['id']))
                    else:
                        sql = """
                              INSERT INTO deputies(id, civil_name, proposition_id, party_initials, created_at, updated_at)
                              VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                              """
                        cursor.execute(sql, (row['id'], row['civil_name'], row['party_initials'], row['proposition_ids']))

                self.conn.commit()
                print("Dados dos deputados inseridos/atualizados com sucesso!")

            except Exception as e:
                print(f"Erro ao inserir/atualizar dados dos deputados: {str(e)}")
                self.conn.rollback()

            finally:
                cursor.close()

    def insert_propositions(self, propositions_df):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                print(propositions_df.columns)

                for index, row in propositions_df.iterrows():
                    cursor.execute("SELECT id FROM propositions WHERE id = %s", (row['id'],))
                    existing_proposition = cursor.fetchone()

                    if existing_proposition:
                        sql = """
                              UPDATE propositions
                              SET type = %s, summary = %s, updated_at = CURRENT_TIMESTAMP
                              WHERE id = %s
                              """
                        cursor.execute(sql, (row['type'], row['summary'], row['id']))
                    else:
                        sql = """
                              INSERT INTO propositions(id, type, summary, created_at, updated_at)
                              VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                              """
                        cursor.execute(sql, (row['id'], row['type'], row['summary']))

                self.conn.commit()
                print("Dados das proposições inseridos/atualizados com sucesso!")

            except Exception as e:
                print(f"Erro ao inserir/atualizar dados das proposições: {str(e)}")
                self.conn.rollback()

            finally:
                cursor.close()

    def insert_themes(self, themes_df):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                print(themes_df.columns)

                for index, row in themes_df.iterrows():
                    cursor.execute("SELECT id FROM themes WHERE proposition_id = %s AND theme = %s",
                                   (row['proposition_id'], row['theme']))
                    existing_theme = cursor.fetchone()

                    if existing_theme:
                        sql = """
                              UPDATE themes
                              SET updated_at = CURRENT_TIMESTAMP
                              WHERE proposition_id = %s AND theme = %s
                              """
                        cursor.execute(sql, (row['proposition_id'], row['theme']))
                    else:
                        sql = """
                              INSERT INTO themes(proposition_id, theme, created_at, updated_at)
                              VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                              """
                        cursor.execute(sql, (row['proposition_id'], row['theme']))

                self.conn.commit()
                print("Dados dos temas inseridos/atualizados com sucesso!")

            except Exception as e:
                print(f"Erro ao inserir/atualizar dados dos temas: {str(e)}")
                self.conn.rollback()

            finally:
                cursor.close()

    def insert_votes(self, votes_df):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                print(votes_df.columns)

                for index, row in votes_df.iterrows():
                    cursor.execute("SELECT id FROM votes WHERE id = %s", (row['id'],))
                    existing_vote = cursor.fetchone()

                    if existing_vote:
                        sql = """
                              UPDATE votes
                              SET proposition_id = %s, description = %s, approval = %s, updated_at = CURRENT_TIMESTAMP
                              WHERE id = %s
                              """
                        cursor.execute(sql, (row['proposition_id'], row['description'], row['approval'], row['id']))
                    else:
                        sql = """
                              INSERT INTO votes(id, proposition_id, description, approval, created_at, updated_at)
                              VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                              """
                        cursor.execute(sql, (row['id'], row['proposition_id'], row['description'], row['approval']))

                self.conn.commit()
                print("Dados dos votos inseridos/atualizados com sucesso!")

            except Exception as e:
                print(f"Erro ao inserir/atualizar dados dos votos: {str(e)}")
                self.conn.rollback()

            finally:
                cursor.close()

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Conexão com PostgreSQL fechada.")