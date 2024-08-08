class CreateDeputiesPropositions < ActiveRecord::Migration[7.1]
  def change
    create_table :deputies_propositions do |t|
      t.references :deputy, null: false, foreign_key: true
      t.references :proposition, null: false, foreign_key: true

      t.timestamps
    end
  end
end
