from db_config import connection_db

class Process:
    def __init__(self, deputy, proposition):
        self.deputy = deputy
        self.proposition = proposition
        db = connection_db()
        self.conn = db.create_connection()

    def insert_deputies(self, deputies_df, propositions_df):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                print(deputies_df.columns)

                for index, row in deputies_df.iterrows() and propositions_df.iterrows():
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
                              INSERT INTO deputies(id, civil_name, party_initials, proposition_id, created_at, updated_at)
                              VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                              """
                        cursor.execute(sql, (row['id'], row['civil_name'], row['party_initials'], row['proposition_id']))

                self.conn.commit()
                print("Dados dos deputados inseridos com sucesso!")

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

    def insert_themes(self, themes_df, propositions_df):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                print(themes_df.columns)

                for index, row in themes_df.iterrows() and propositions_df.iterrows():
                    cursor.execute("SELECT id FROM themes WHERE id = %s", (row['id'],))
                    existing_theme = cursor.fetchone()

                    if existing_theme:
                        sql = """
                              UPDATE themes
                              SET theme = %s, proposition_id = %s, updated_at = CURRENT_TIMESTAMP
                              WHERE id = %s
                              """
                        cursor.execute(sql, (row['theme'], row['proposition_id'], row['id']))
                    else:
                        sql = """
                              INSERT INTO themes(id, proposition_id, theme, created_at, updated_at)
                              VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                              """
                        cursor.execute(sql, (row['id'], row['proposition_id'], row['theme']))

                self.conn.commit()
                print("Dados dos temas inseridos/atualizados com sucesso!")

            except Exception as e:
                print(f"Erro ao inserir/atualizar dados dos temas: {str(e)}")
                self.conn.rollback()

            finally:
                cursor.close()

    def insert_votes(self, votes_df, propositions_df):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                print(votes_df.columns)

                for index, row in votes_df.iterrows() and propositions_df.iterrows():
                    cursor.execute("SELECT id FROM votes WHERE id = %s", (row['id'],))
                    existing_vote = cursor.fetchone()

                    if existing_vote:
                        sql = """
                              UPDATE votes
                              SET vote_id = %s, description = %s, approval = %s, updated_at = CURRENT_TIMESTAMP
                              WHERE id = %s
                              """
                        cursor.execute(sql, (row['vote_id'], row['description'], row['approval']))
                    else:
                        sql = """
                              INSERT INTO votes(id, proposition_id, description, approval, created_at, updated_at)
                              VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                              """
                        cursor.execute(sql, (row['vote_id'], row['description'], row['proposition_id'], row['approval']))

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