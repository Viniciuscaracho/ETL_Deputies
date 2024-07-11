class CreateDeputies < ActiveRecord::Migration[7.1]
  def change
    create_table :deputies do |t|
      t.string :civil_name
      t.string :party_initials

      t.timestamps
    end
  end
end
