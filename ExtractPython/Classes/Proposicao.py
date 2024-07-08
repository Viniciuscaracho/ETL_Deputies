import requests
import pandas as pd
from Classes.Deputado import Deputado
class Proposicao:
    def __init__(self, id):
        self.id = id
        self.base_url = "https://dadosabertos.camara.leg.br/api/v2/"

    def get_proposicao(self, id_proposicao):
        response = requests.get(f"{self.base_url}/proposicoes/{id_proposicao}")
        return response.json()

    def get_detalhes(self):
        response = requests.get(f"{self.base_url}/proposicoes/{self.id}")
        return response.json()

    def get_temas(self):
        response = requests.get(f"{self.base_url}/proposicoes/{self.id}/temas")
        response_temas = response.json()
        temas_list = []

        if "dados" in response_temas:
            for tema in response_temas["dados"]:
                temas_list.append({
                    "proposicao_id": self.id,
                    "tema": tema['tema']
                })

        df_temas = pd.DataFrame(temas_list)
        return df_temas

    def get_votos(self):
        response = requests.get(f"{self.base_url}/proposicoes/{self.id}/votacoes")
        response_votos = response.json()
        votos_list = []

        if "dados" in response_votos:
            for voto in response_votos["dados"]:
                votos_list.append({
                    "voto_id": voto["id"],
                    "descricao": voto['descricao'],
                    "aprovacao": voto['aprovacao']
                })

        df_votos = pd.DataFrame(votos_list)
        return df_votos
