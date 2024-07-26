# frozen_string_literal: true

class Vote < ApplicationRecord
  # Associations
  belongs_to :proposition

  # Validations
  validates :description, presence: true
  validates :approval, presence: true
  validates :proposition_id, presence: true
end