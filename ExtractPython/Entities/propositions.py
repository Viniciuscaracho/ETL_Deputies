import requests
import pandas as pd
import os

class Proposition:
    def __init__(self, deputy):
        self.deputy = deputy
        self.base_url = "https://dadosabertos.camara.leg.br/api/v2/"
        self.selected_propositions_df = self.deputy.get_propositions()

    def chunks(self, lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def get_proposition_authors(self, batch_size=100):
        authors_list = []
        for batch in self.chunks(self.selected_propositions_df['id'], batch_size):
            for proposition_id in batch:
                try:
                    response = requests.get(f"{self.base_url}/proposicoes/{proposition_id}/autores")
                    response.raise_for_status()
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching authors for proposition {proposition_id}: {str(e)}")
                    continue

                response_data = response.json()
                if 'dados' not in response_data:
                    print(f"No authors found for proposition {proposition_id}")
                    continue

                for author in response_data['dados']:
                    if '/orgaos/' in author["uri"]:
                        continue
                    authors_list.append({
                        "uri": author["uri"],
                        "name": author["nome"],
                        "proposition_id": proposition_id,
                    })

        return pd.DataFrame(authors_list)

    def get_themes(self, batch_size=100):
        if self.selected_propositions_df.empty:
            raise ValueError("No propositions data found")

        themes_list = []
        for batch in self.chunks(self.selected_propositions_df['id'], batch_size):
            for proposition_id in batch:
                try:
                    response = requests.get(f"{self.base_url}/proposicoes/{proposition_id}/temas")
                    response.raise_for_status()
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching themes for proposition {proposition_id}: {str(e)}")
                    continue

                response_data = response.json()
                if 'dados' not in response_data:
                    print(f"No themes found for proposition {proposition_id}")
                    continue

                for theme in response_data['dados']:
                    themes_list.append({
                        "proposition_id": proposition_id,
                        "theme": theme['tema']
                    })

        themes_df = pd.DataFrame(themes_list)
        themes_df['id'] = themes_df.index

        return themes_df

    def get_votes(self, batch_size=100):
        if self.selected_propositions_df.empty:
            raise ValueError("No propositions data found")

        votes_list = []
        for batch in self.chunks(self.selected_propositions_df['id'], batch_size):
            for proposition_id in batch:
                try:
                    response = requests.get(f"{self.base_url}/proposicoes/{proposition_id}/votacoes")
                    response.raise_for_status()
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching votes for proposition {proposition_id}: {str(e)}")
                    continue

                response_data = response.json()
                if 'dados' not in response_data:
                    print(f"No votes found for proposition {proposition_id}")
                    continue

                for vote in response_data['dados']:
                    votes_list.append({
                        "id": vote["id"],
                        "proposition_id": proposition_id,
                        "description": vote['descricao'],
                        "approval": vote["aprovacao"]
                    })

        return pd.DataFrame(votes_list)