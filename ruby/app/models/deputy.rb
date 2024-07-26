# frozen_string_literal: true

class Deputy < ApplicationRecord
  # Associations
  # has_many :propositions, foreign_key: :proposition_id

  # Validations
  validates :civil_name, presence: true
  validates :party_initials, presence: true
end