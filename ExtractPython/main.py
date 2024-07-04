from Classes.Deputado import Deputado
from Classes.Proposicao import Proposicao
from Extract.Processamento import Processamento
import pandas as pd

deputado = Deputado(220682)
proposicao = Proposicao(deputado)

detalhes_deputado = deputado.get_detalhes()
proposicoes = deputado.get_proposicoes()
# temas_proposicoes = proposicao.get_temas()
# votos_deputado = proposicao.get_votacoes()


df_detalhes_deputados = pd.DataFrame([{
     "id": detalhes_deputado["dados"]["id"],
    "nome": detalhes_deputado["dados"]["ultimoStatus"]["nome"]
}])
print(df_detalhes_deputados)

proposicoes_dados = proposicoes['dados']
df_proposicoes = pd.DataFrame(proposicoes_dados)
df_proposicoes_selecionado = df_proposicoes[['id', 'siglaTipo', 'ementa']]
print(df_proposicoes_selecionado)

# df_temas_proposicoes = pd.DataFrame([{
#      "id": detalhes_deputado["dados"]["id"],
#     "nome": detalhes_deputado["dados"]["ultimoStatus"]["nome"]
# }])
#
# df_votos_deputado = pd.DataFrame([{
#      "id": detalhes_deputado["dados"]["id"],
#     "nome": detalhes_deputado["dados"]["ultimoStatus"]["nome"]
# }])


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