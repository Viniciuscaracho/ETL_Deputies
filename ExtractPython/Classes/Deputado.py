import requests
from Classes.Proposicao import Proposicao
class Deputado:
    def __init__(self, id):
        self.id = id
        self.base_url = "https://dadosabertos.camara.leg.br/api/v2/"

    def get_detalhes(self):
        response = requests.get(f"{self.base_url}/deputados/{self.id}")
        return response.json()

    def get_proposicoes_autor(self):
        response = requests.get(f"{self.base_url}/proposicoes?autor={self.id}")
        proposicoes_data = response.json()['dados']  # Acessa apenas a lista de proposições

        proposicoes = []
        for prop_data in proposicoes_data:
            proposicao = Proposicao(prop_data['id'])
            proposicoes.append(proposicao)

        return proposicoes

    def get_votos(self):
        response = requests.get(f"{self.base_url}/deputados/{self.id}/votos")
        return response.json()

    def get_temas_proposicoes(self):
        proposicoes = self.get_proposicoes_autor()
        temas = {}
        for prop in proposicoes:
            temas[prop.id] = prop.get_proposicao(prop.id)
        return temas