from Entities.deputy import Deputy
from Entities.propositions import Proposition
from Extract.process import Process

if __name__ == '__main__':
    deputy = Deputy()
    proposicao = Proposition(deputy)
    process = Process(deputy, proposicao)

    autores = proposicao.get_proposition_authors()
    deputados = deputy.get_deputies(autores)
    process.insert_deputies(deputados)
    # print(deputados)
    # selected_propositions_df = deputy.get_deputy_propositions()
    # process.insert_propositions(selected_propositions_df)

    # temas = proposicao.get_themes()
    # process.insert_themes(temas)
    #
    # votos = proposicao.get_votes()
    # process.insert_votes(votos)
