import requests
from Classes.Proposicao import Proposicao

class Deputado:
    def __init__(self, id):
        self.id = id
        self.base_url = "https://dadosabertos.camara.leg.br/api/v2/"

    def get_detalhes(self):
        response = requests.get(f"{self.base_url}/deputados/{self.id}")
        return response.json()

    def get_proposicoes(self):
        response = requests.get(f"{self.base_url}/proposicoes/")
        return response.json()
