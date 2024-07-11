class CreatePropositionThemes < ActiveRecord::Migration[7.1]
  def change
    create_table :proposition_themes do |t|
      t.references :proposition, null: false, foreign_key: true
      t.references :theme, null: false, foreign_key: true

      t.timestamps
    end
  end
end
