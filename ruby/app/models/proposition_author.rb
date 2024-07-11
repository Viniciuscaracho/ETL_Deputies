class PropositionAuthor < ApplicationRecord
  belongs_to :deputy
  belongs_to :proposition
end
