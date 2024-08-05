import requests
import pandas as pd
import os


class Deputy:
    def __init__(self):
        self.base_url = "https://dadosabertos.camara.leg.br/api/v2/"

    def get_deputies(self, authors_df):
        deputies_list = []
        unique_uris = authors_df['uri'].drop_duplicates()

        for author_uri in unique_uris:
            try:
                response = requests.get(author_uri)
                response.raise_for_status()
                response_data = response.json()['dados']
                author_propositions = authors_df[authors_df['uri'] == author_uri]['proposition_id'].tolist()
                selected_deputy = {
                    'id': response_data['id'],
                    'civil_name': response_data['nomeCivil'],
                    'party_initials': response_data['ultimoStatus']['siglaPartido'],
                    'proposition_ids': author_propositions
                }
                deputies_list.append(selected_deputy)
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data from {author_uri}: {str(e)}")

        deputies_df = pd.DataFrame(deputies_list).explode('proposition_ids').drop_duplicates(subset=['id', 'proposition_ids'])
        return deputies_df

    def get_deputy_propositions(self, max_rows=300):
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
                'id': prop.get('id'),
                'proposition_type': prop.get('siglaTipo'),
                'summary': prop.get('ementa'),
                'uriRelator': prop.get('uriRelator')
            }
            propositions_list.append(current_proposition)
            if len(propositions_list) >= max_rows:
                break

        return pd.DataFrame(propositions_list)