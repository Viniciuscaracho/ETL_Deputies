class Proposition < ApplicationRecord
  has_many :votes
  has_many :proposition_authors
  has_many :deputies, through: :proposition_authors
  has_many :proposition_themes
  has_many :themes, through: :proposition_themes
end
