from Classes.Deputado import Deputado
from Classes.Proposicao import Proposicao

deputado = Deputado(73453)
proposicao = Proposicao(deputado)

print(deputado.get_proposicoes())
print(proposicao.get_proposicao_autores())
print(deputado.get_detalhes())
print(proposicao.get_temas())
print(proposicao.get_votos())



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

