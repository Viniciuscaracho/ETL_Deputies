class RenameTypeColumnInPropositions < ActiveRecord::Migration[7.1]
  def change
    rename_column :propositions, :type, :proposition_type
  end
end
