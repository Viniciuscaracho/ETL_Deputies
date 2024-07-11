class CreateVotes < ActiveRecord::Migration[7.1]
  def change
    create_table :votes do |t|
      t.references :proposition, null: false, foreign_key: true
      t.text :description
      t.string :approval

      t.timestamps
    end
  end
end
