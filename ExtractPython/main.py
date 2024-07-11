from Entities.deputy import Deputy
from Entities.propositions import Proposition
from Extract.process import Process

if __name__ == '__main__':
    deputado = Deputy()
    proposicao = Proposition(deputado)
    processamento = Process(deputado, proposicao)
    processamento.processar()
