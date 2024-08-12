# frozen_string_literal: true

class Deputy < ApplicationRecord
  # Associations
  include PgSearch::Model
  pg_search_scope :search_by_name_and_party,
                  against: [:civil_name, :party_initials],
                  using: {
                    tsearch: { prefix: true }
                  }
  has_many :deputies_propositions
  has_many :propositions, through: :deputies_propositions

  # Validations
  validates :civil_name, presence: true
  validates :party_initials, presence: true
end