import requests
import pandas as pd
import os

class Deputy:
    def __init__(self):
        self.id = None
        self.base_url = "https://dadosabertos.camara.leg.br/api/v2/"

    def get_deputies(self, proposition):
        deputies_list = []

        for author_uri in proposition['uri']:
            try:
                response = requests.get(author_uri)
                response.raise_for_status()  # Raise exception for bad response status
                response_data = response.json()['dados']
                selected_deputy = {
                    'id': response_data['id'],
                    'civil_name': response_data['nomeCivil'],
                    'party_initials': response_data['ultimoStatus']['siglaPartido']
                }
                deputies_list.append(selected_deputy)
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data from {author_uri}: {str(e)}")

        return pd.DataFrame(deputies_list)

    def get_propositions(self, max_rows=40):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, '../proposicoes-2024.json')

        try:
            propositions = pd.read_json(file_path)
        except FileNotFoundError as e:
            print(f"File not found error: {str(e)}")
            return pd.DataFrame()

        propositions_list = []

        for prop in propositions['dados']:
            current_proposition = {
                'id': prop['id'],
                'type_initials': prop['siglaTipo'],
                'summary': prop['ementa']
            }
            propositions_list.append(current_proposition)
            if len(propositions_list) >= max_rows:
                break

        return pd.DataFrame(propositions_list)