class CreatePropositions < ActiveRecord::Migration[7.1]
  def change
    create_table :propositions do |t|
      t.text :description

      t.timestamps
    end
  end
end
