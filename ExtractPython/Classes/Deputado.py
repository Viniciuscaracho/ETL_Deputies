import requests
import pandas as pd
from Classes.Proposicao import Proposicao

class Deputado:
    def __init__(self, id):
        self.id = id
        self.base_url = "https://dadosabertos.camara.leg.br/api/v2/"


    def get_deputados(self):
        response = requests.get(f"{self.base_url}/deputados/")
        deputados = []
        for deput in

    def get_detalhes(self):
        response = requests.get(f"{self.base_url}/deputados/{self.id}")
        detalhes_deputado = response.json()
        df_detalhes_deputados = pd.DataFrame([{
            "id": detalhes_deputado["dados"]["id"],
            "nome": detalhes_deputado["dados"]["ultimoStatus"]["nome"]
        }])
        return df_detalhes_deputados

    def get_proposicoes(self):
        response = requests.get(f"{self.base_url}/proposicoes/")
        proposicoes = response.json()
        proposicoes_dados = proposicoes['dados']
        df_proposicoes = pd.DataFrame(proposicoes_dados)
        df_proposicoes_selecionado = df_proposicoes[['id', 'siglaTipo', 'ementa']]
        return df_proposicoes_selecionado
