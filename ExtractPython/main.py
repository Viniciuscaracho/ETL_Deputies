from Entities.deputy import Deputy
from Entities.propositions import Proposition
from Extract.Processamento import Processamento

if __name__ == '__main__':
    deputado = Deputy()
    proposicao = Proposition(deputado)
    processamento = Processamento(deputado, proposicao)
    processamento.processar()
