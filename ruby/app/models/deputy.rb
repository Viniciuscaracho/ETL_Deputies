require 'pg_search'
class Deputy < ApplicationRecord
  include PgSearch::Model
  pg_search_scope :search_by_name_and_party,
                  against: [:civil_name, :party_initials],
                  using: {
                    tsearch: { prefix: true }
                  }
end
