from Entities.deputy import Deputy
from Entities.propositions import Proposition
from Extract.process import Process

if __name__ == '__main__':
    deputy = Deputy()
    proposition = Proposition(deputy)
    process = Process(deputy, proposition)

    propositions_df = proposition.get_propositions()

    authors_df = proposition.get_proposition_authors()
    deputies_df = deputy.get_deputies(authors_df)
    process.insert_propositions(propositions_df)
    process.insert_deputies(deputies_df)


    process.close_connection()