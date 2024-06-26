import pandas as pd
import os

class Processamento:
    def __init__(self, entrada):
        self.entrada = entrada

    def processar(self):
        
        for arquivo_entrada in self.entrada:
            nome_base = os.path.basename(arquivo_entrada).split('.')[0]

            df = pd.read_csv(arquivo_entrada, delimiter=';', quotechar='"')

            if nome_base == 'votacoesProposicoes-2024':
                colunas_necessarias = ["proposicao_id", "descricao"]
            elif nome_base == 'votacoesObjetos-2024':
                colunas_necessarias = ["proposicao_id", "descricao"]
            elif nome_base == 'proposicoesTemas-2024':
                colunas_necessarias = ["uriProposicao", "tema"]
            elif nome_base == 'proposicoesAutores-2024':
                colunas_necessarias = ["idProposicao", "idDeputadoAutor", "nomeAutor"]
            else:
                print(f"Arquivo {arquivo_entrada} não reconhecido.")
                continue

            # Verifica se todas as colunas necessárias estão presentes no DataFrame
            if all(coluna in df.columns for coluna in colunas_necessarias):
                df_selecionado = df[colunas_necessarias]

                # Salvar o DataFrame em um novo arquivo CSV
                df_selecionado.to_csv(f"{nome_base}_results.csv", index=False)

                # Criar uma lista e um dicionário baseado nas colunas principais
                coluna_chave = colunas_necessarias[0]
                coluna_valor = colunas_necessarias[1] if len(colunas_necessarias) > 1 else None

                lista_chave = df_selecionado[coluna_chave].tolist()
                dicionario_valor = df_selecionado.set_index(coluna_chave)[
                    coluna_valor].to_dict() if coluna_valor else None

                # Exibe a lista e o dicionário (opcional)
                print(f"Lista de {nome_base}:", lista_chave)
                if dicionario_valor:
                    print(f"Dicionário de {nome_base}:", dicionario_valor)
            else:
                print(f"O arquivo {arquivo_entrada} não contém todas as colunas necessárias: {colunas_necessarias}")