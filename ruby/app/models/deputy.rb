# frozen_string_literal: true

class Deputy < ApplicationRecord
  # Associations
  include PgSearch::Model
  pg_search_scope :search_by_name_and_party,
                  against: [:civil_name, :party_initials],
                  using: {
                    tsearch: { prefix: true }
                  }
  has_many :propositions, foreign_key: :deputy_id, primary_key: :id

  # Validations
  validates :civil_name, presence: true
  validates :party_initials, presence: true
end