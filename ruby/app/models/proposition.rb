# frozen_string_literal: true

class Proposition < ApplicationRecord
  # Associations
  # has_many :themes
  # has_many :votes

  # Validations
  validates :type, presence: true
  validates :summary, presence: true
end