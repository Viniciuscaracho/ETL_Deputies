import pandas as pd

class Processamento:
    def __init__(self, entrada):
        self.entrada = entrada

    def processar(self):
        for item in self.entrada:
            nome_base = item['nome_base']
            dados = item['dados']

            if isinstance(dados, list):
                # Se os dados são uma lista de dicionários, criamos o DataFrame diretamente
                df = pd.DataFrame(dados)
            elif isinstance(dados, dict):
                # Se os dados são um dicionário, convertemos para uma lista de dicionários
                df = pd.DataFrame([dados])
            else:
                print(f"Tipo de dados não suportado para {nome_base}: {type(dados)}")
                continue

            if nome_base == 'detalhes_deputado':
                colunas_necessarias = ["id", "nome", "siglaPartido"]
            elif nome_base == 'votos_deputado':
                colunas_necessarias = ["proposicao_id", "voto"]
            elif nome_base == 'temas_proposicoes':
                colunas_necessarias = ["proposicao_id", "tema"]
            elif nome_base == 'proposicoes_autor':
                colunas_necessarias = ["id", "ementa"]
            else:
                print(f"Dados {nome_base} não reconhecidos.")
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
                print(f"Os dados {nome_base} não contêm todas as colunas necessárias: {colunas_necessarias}")