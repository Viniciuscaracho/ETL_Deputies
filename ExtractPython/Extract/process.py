from db_config import connection_db
from sqlalchemy import create_engine

class Process:
    def __init__(self, deputy, proposition):
        self.deputy = deputy
        self.proposition = proposition
        db = connection_db()
        self.engine = create_engine(f'postgresql://{db.DB_USER}:{db.DB_PASSWORD}@{db.DB_HOST}:{db.DB_PORT}/{db.DB_NAME}')


    def insert_deputies(self, deputies_df):
        deputies_df.to_sql('deputies', con=self.engine, if_exists='append', index=False)

    def insert_propositions(self, propositions_df):
        propositions_df.to_sql('propositions', con=self.engine, if_exists='append', index=False)

    def insert_authors(self, authors_df):
        authors_df.to_sql('authors', con=self.engine, if_exists='append', index=False)

    def insert_themes(self, themes_df):
        themes_df.to_sql('themes', con=self.engine, if_exists='append', index=False)

    def insert_votes(self, votes_df):
        votes_df.to_sql('votes', con=self.engine, if_exists='append', index=False)