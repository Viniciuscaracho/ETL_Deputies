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
        deputado = Deputado(220682)
        df_proposicoes_selecionado = deputado.get_proposicoes()

        for proposicao_id in df_proposicoes_selecionado['id']:
            proposicao = Proposicao(proposicao_id)
            temas_proposicao = proposicao.get_temas()
            for tema in temas_proposicao['dados']:
                temas_list.append({
                    "proposicao_id": proposicao_id,
                    "tema": tema['tema']
                })

        df_temas = pd.DataFrame(temas_list)
        return df_temas

    def get_votos(self):
        response = requests.get(f"{self.base_url}/proposicoes/{self.id}/votacoes")
        deputado = Deputado(220682)
        df_proposicoes_selecionado = deputado.get_proposicoes()
        votos_list = []
        for proposicoes_id in df_proposicoes_selecionado['id']:
            proposicao = Proposicao(proposicoes_id)
            votos_deputado = proposicao.get_votos()
            for voto in votos_deputado['dados']:
                votos_list.append({
                    "voto_id": voto["id"],
                    "descricao": voto['descricao'],
                    "aprovacao": voto['aprovacao']
                })
        df_votos = pd.DataFrame(votos_list)
        return df_votos

