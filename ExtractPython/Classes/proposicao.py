import requests
import pandas as pd

class Proposicao:
    def __init__(self, deputado):
        self.deputado = deputado
        self.base_url = "https://dadosabertos.camara.leg.br/api/v2/"
        self.df_proposicoes_selecionado = self.deputado.get_proposicoes()


    def get_proposicao_autores(self):
        autores_list = []
        for proposicao_id in self.df_proposicoes_selecionado['id']:
            response = requests.get(f"{self.base_url}/proposicoes/{proposicao_id}/autores")

            if response.status_code != 200:
                print(f"Failed to fetch temas for proposicao {proposicao_id}: {response.status_code}")
                continue

            response_autores = response.json()
            if 'dados' not in response_autores:
                print(f"No temas found for proposicao {proposicao_id}")
                continue

            for autores in response_autores['dados']:
                autores_list.append({
                    "uri": autores["uri"],
                    "nome": autores["nome"]
                })

        df_autores = pd.DataFrame(autores_list)
        return df_autores

    def get_temas(self):
        if self.df_proposicoes_selecionado.empty:
            raise ValueError("No proposicoes data found")

        temas_list = []
        for proposicao_id in self.df_proposicoes_selecionado['id']:
            response = requests.get(f"{self.base_url}/proposicoes/{proposicao_id}/temas")
            if response.status_code != 200:
                print(f"Failed to fetch temas for proposicao {proposicao_id}: {response.status_code}")
                continue

            response_temas = response.json()
            if 'dados' not in response_temas:
                print(f"No temas found for proposicao {proposicao_id}")
                continue

            for tema in response_temas['dados']:
                temas_list.append({
                    "proposicao_id": proposicao_id,
                    "tema": tema['tema']
                })

        df_temas = pd.DataFrame(temas_list)
        return df_temas

    def get_votos(self):
        if self.df_proposicoes_selecionado.empty:
            raise ValueError("No proposicoes data found")

        votos_list = []
        for proposicao_id in self.df_proposicoes_selecionado['id']:
            response = requests.get(f"{self.base_url}/proposicoes/{proposicao_id}/votacoes")
            if response.status_code != 200:
                print(f"Failed to fetch temas for proposicao {proposicao_id}: {response.status_code}")
                continue

            response_temas = response.json()
            if 'dados' not in response_temas:
                print(f"No temas found for proposicao {proposicao_id}")
                continue

            for voto in response_temas['dados']:
                votos_list.append({
                    "voto_id": voto["id"],
                    "descricao": voto['descricao'],
                    "aprovacao": voto["aprovacao"]
                })

        df_votos = pd.DataFrame(votos_list)
        return df_votos

