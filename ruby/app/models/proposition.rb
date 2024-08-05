# frozen_string_literal: true

class Proposition < ApplicationRecord
  # Associations
  has_many :themes
  has_many :votes
  belongs_to :deputy

  # Validations
  validates :type, presence: true
  validates :summary, presence: true
end