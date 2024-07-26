class CreateThemes < ActiveRecord::Migration[7.1]
  def change
    create_table :themes do |t|
      t.integer :proposition_id
      t.string :theme

      t.timestamps
    end
  end
end
