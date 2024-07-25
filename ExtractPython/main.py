from Entities.deputy import Deputy
from Entities.propositions import Proposition
from Extract.process import Process

if __name__ == '__main__':
    deputy = Deputy()
    proposition = Proposition(deputy)
    process = Process(deputy, proposition)

    authors = proposition.get_proposition_authors()
    deputies = deputy.get_deputies(authors)
    propositions = deputy.get_deputy_propositions()
    process.insert_propositions(propositions)
    process.insert_deputies(deputies, propositions)
    process.insert_votes(proposition.get_votes(), propositions)
    process.insert_themes(proposition.get_themes(), propositions)
    process.close_connection()