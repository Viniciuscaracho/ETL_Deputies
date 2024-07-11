class Deputy < ApplicationRecord
  has_many :proposition_authors
  has_many :propositions, through: :proposition_authors
end
