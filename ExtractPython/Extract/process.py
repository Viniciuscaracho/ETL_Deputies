from db import connection_db

class Process:
    def __init__(self, deputy, proposition):
        self.deputy = deputy
        self.proposition = proposition

    def processar(self):
        db = connection_db()
        conn = db.create_connection()
        if conn:
            authors = self.proposition.get_proposition_authors()
            df_deputy = self.deputy.get_deputies(authors)
            df_deputy.to_sql('deputies', con=conn, if_exists='replace')
            df_proposition = self.proposition.get_propositions()
            df_proposition.to_sql('propositions', con=conn, if_exists='replace')
            conn.close()
