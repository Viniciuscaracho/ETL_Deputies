from Classes.Deputado import Deputado
from Extract.Processamento import Processamento

deputado = Deputado(204536)
detalhes_deputado = deputado.get_detalhes()
proposicoes_autor = deputado.get_proposicoes_autor()
temas_proposicoes = deputado.get_temas_proposicoes()
votos_deputado = deputado.get_votos()

print(temas_proposicoes)

# entrada = [
#     {'nome_base': 'detalhes_deputado', 'dados': [detalhes_deputado]},
#     {'nome_base': 'votos_deputado', 'dados': votos_deputado},
#     {'nome_base': 'temas_proposicoes', 'dados': [{'proposicao_id': prop_id, 'tema': tema} for prop_id, temas in temas_proposicoes.items() for tema in temas]},
#     {'nome_base': 'proposicoes_autor', 'dados': [prop.__dict__ for prop in proposicoes_autor]}
# ]
#
# # Execute o processamento
# processamento = Processamento(entrada)
# processamento.processar()