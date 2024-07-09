import requests
import pandas as pd

class Deputado:
    def __init__(self):
        self.id = None
        self.base_url = "https://dadosabertos.camara.leg.br/api/v2/"

    def get_deputados(self, proposicao):
        deputados_list = []

        for autores_uri in proposicao['uri']:
            response = requests.get(autores_uri)
            if response.status_code == 200:
                response_deputados = response.json()
                deputado_info = response_deputados['dados']
                deputados_selecionado = {
                    'id': deputado_info['id'],
                    'nomeCivil': deputado_info['nomeCivil'],
                    'siglaPartido': deputado_info['ultimoStatus']['siglaPartido']
                }
                deputados_list.append(deputados_selecionado)

        result_deputados = pd.DataFrame(deputados_list)
        return result_deputados

    def get_proposicoes(self):
        response = requests.get(f"{self.base_url}/proposicoes/")
        proposicoes = response.json()
        proposicoes_dados = proposicoes['dados']
        df_proposicoes = pd.DataFrame(proposicoes_dados)
        df_proposicoes_selecionado = df_proposicoes[['id', 'siglaTipo', 'ementa']]
        return df_proposicoes_selecionado
