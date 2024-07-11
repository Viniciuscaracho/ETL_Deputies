class CreatePropositionAuthors < ActiveRecord::Migration[7.1]
  def change
    create_table :proposition_authors do |t|
      t.references :deputy, null: false, foreign_key: true
      t.references :proposition, null: false, foreign_key: true

      t.timestamps
    end
  end
end
