# frozen_string_literal: true

class Proposition < ApplicationRecord
  # Associations
  has_many :themes
  has_many :votes
  has_many :deputies_propositions
  has_many :deputies, through: :deputies_propositions
  # Validations
  validates :type, presence: true
  validates :summary, presence: true
end