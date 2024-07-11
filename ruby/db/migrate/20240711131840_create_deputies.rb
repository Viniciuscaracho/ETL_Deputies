class CreateDeputies < ActiveRecord::Migration[7.1]
  def change
    create_table :deputies do |t|
      t.string :name
      t.string :party

      t.timestamps
    end
  end
end
