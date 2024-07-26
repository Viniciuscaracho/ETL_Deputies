# frozen_string_literal: true

class Theme < ApplicationRecord
  # Associations
  belongs_to :proposition

  # Validations
  validates :theme, presence: true
  validates :proposition_id, presence: true
end