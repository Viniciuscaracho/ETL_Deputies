import os
from Extract.Processamento import Processamento

entrada = [os.path.join('fontes', 'proposicoesTemas-2024.csv'),
           os.path.join('fontes', 'votacoesObjetos-2024.csv'),
           os.path.join('fontes', 'votacoesProposicoes-2024.csv'),
           os.path.join('fontes', 'proposicoesAutores-2024.csv')]

processamento = Processamento(entrada)
processamento.processar()
