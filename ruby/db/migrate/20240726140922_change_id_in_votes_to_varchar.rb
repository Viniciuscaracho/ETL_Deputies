class ChangeIdInVotesToVarchar < ActiveRecord::Migration[7.1]
  def change
    change_column :votes, :id, :string

    add_index :votes, :id, unique: true
  end
end
