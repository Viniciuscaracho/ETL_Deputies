class CreateThemes < ActiveRecord::Migration[7.1]
  def change
    create_table :themes do |t|
      t.references :proposition, null: false, foreign_key: true
      t.text :theme

      t.timestamps
    end
  end
end
