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
        # Itera sobre os IDs das proposições em lotes
        for batch in self.chunks(self.selected_propositions_df['id'], batch_size):
            for proposition_id in batch:
                try:
                    response = requests.get(f"{self.base_url}/proposicoes/{proposition_id}/autores")
                    response.raise_for_status()
                except requests.exceptions.RequestException as e:
                    # Tratamento de erro em caso de falha na solicitação
                    print(f"Error fetching authors for proposition {proposition_id}: {str(e)}")
                    continue

                response_data = response.json()
                if 'dados' not in response_data:
                    # Caso não haja dados de autores na resposta
                    print(f"No authors found for proposition {proposition_id}")
                    continue

                # Adiciona cada autor à lista de autores, ignorando órgãos
                for author in response_data['dados']:
                    if '/orgaos/' in author["uri"]:
                        continue
                    authors_list.append({
                        "uri": author["uri"],
                        "name": author["nome"],
                        "proposition_id": proposition_id,
                    })

        return pd.DataFrame(authors_list)

    def get_propositions(self, max_rows=500):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, '../Ano-2024.json')

        try:
            # Tenta ler as proposições do arquivo JSON local
            propositions = pd.read_json(file_path)
        except FileNotFoundError as e:
            # Tratamento de erro para arquivo não encontrado
            print(f"File not found error: {str(e)}")
            return pd.DataFrame()
        except ValueError as e:
            # Tratamento de erro para problemas na leitura do JSON
            print(f"Error reading JSON file: {str(e)}")
            return pd.DataFrame()

        if 'dados' not in propositions.columns:
            # Verifica se o JSON possui a estrutura esperada
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

        # Solicita proposições adicionais da API
        api_url = f"{self.base_url}/proposicoes"
        response = requests.get(api_url, params={'itens': max_rows})

        if response.status_code == 200:
            api_data = response.json().get('dados', [])
            for prop in api_data:
                current_proposition = {
                    'id': prop['id'],
                    'proposition_type': prop['siglaTipo'],
                    'summary': prop['ementa']
                }
                propositions_list.append(current_proposition)
                if max_rows <= len(propositions_list):
                    break
        else:
            print(f"API request failed with status code: {response.status_code}")

        return pd.DataFrame(propositions_list)