from Classes.Deputado import Deputado
from Classes.Proposicao import Proposicao
from Extract.Processamento import Processamento
import pandas as pd

deputado = Deputado(220682)
proposicao = Proposicao(deputado)

# detalhes_deputado = deputado.get_detalhes()
#
# df_detalhes_deputados = pd.DataFrame([{
#      "id": detalhes_deputado["dados"]["id"],
#     "nome": detalhes_deputado["dados"]["ultimoStatus"]["nome"]
# }])
# print(df_detalhes_deputados)

# proposicoes = deputado.get_proposicoes()
# proposicoes_dados = proposicoes['dados']
# df_proposicoes = pd.DataFrame(proposicoes_dados)
# df_proposicoes_selecionado = df_proposicoes[['id', 'siglaTipo', 'ementa']]
# print(df_proposicoes_selecionado)

# temas_list = []
# for proposicao_id in df_proposicoes_selecionado['id']:
#     proposicao = Proposicao(proposicao_id)
#     temas_proposicao = proposicao.get_temas()
#     for tema in temas_proposicao['dados']:
#         temas_list.append({
#             "proposicao_id": proposicao_id,
#             "tema": tema['tema']
#         })
#
# df_temas = pd.DataFrame(temas_list)
# print(df_temas)

# votos_list = []
# for proposicoes_id in df_proposicoes_selecionado['id']:
#     proposicao = Proposicao(proposicoes_id)
#     votos_deputado = proposicao.get_votos()
#     for voto in votos_deputado['dados']:
#         votos_list.append({
#             "voto_id": voto["id"],
#             "descricao": voto['descricao'],
#             "aprovacao": voto['aprovacao']
#         })
# df_votos = pd.DataFrame(votos_list)
# print(df_votos.query("aprovacao == 1.0"))

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