class ChangePropositionIdToBeString < ActiveRecord::Migration[7.1]
  def change
    change_column :deputies, :proposition_id, :string
    change_column :votes, :proposition_id, :string
  end
end