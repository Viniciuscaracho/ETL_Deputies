import requests
import pandas as pd
import os

class Proposition:
    def __init__(self, deputy):
        self.deputy = deputy
        self.base_url = "https://dadosabertos.camara.leg.br/api/v2/"
        self.selected_propositions_df = self.get_propositions()

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

    def get_propositions(self, max_rows=200):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, '../proposicoes-2024.json')

        try:
            propositions = pd.read_json(file_path)
        except FileNotFoundError as e:
            print(f"File not found error: {str(e)}")
            return pd.DataFrame()
        except ValueError as e:
            print(f"Error reading JSON file: {str(e)}")
            return pd.DataFrame()

        if 'dados' not in propositions.columns:
            print("Unexpected JSON structure.")
            return pd.DataFrame()

        propositions_list = []

        for prop in propositions['dados']:
            current_proposition = {
                'id': prop['id'],
                'proposition_type': prop['siglaTipo'],
                'summary': prop['ementa']
            }
            propositions_list.append(current_proposition)
            if max_rows <= len(propositions_list):
                break
        return pd.DataFrame(propositions_list)
