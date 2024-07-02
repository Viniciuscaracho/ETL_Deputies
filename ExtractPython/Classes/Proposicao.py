import requests
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
        return response.json()

    def get_votacoes(self):
        response = requests.get(f"{self.base_url}/proposicoes/{self.id}/votacoes")
        return response.json()

