from Classes.deputado import Deputado
from Classes.proposicao import Proposicao

deputado = Deputado()
proposicao = Proposicao(deputado)
autores = proposicao.get_proposicao_autores()
print(autores.to_string(index=False))
deputados = deputado.get_deputados(autores)
print(deputados.to_string(index=False))
print(proposicao.get_votos())
print(proposicao.get_temas())
