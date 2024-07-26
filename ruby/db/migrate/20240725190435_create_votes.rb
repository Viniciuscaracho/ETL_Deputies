class CreateVotes < ActiveRecord::Migration[7.1]
  def change
    create_table :votes do |t|
      t.integer :proposition_id
      t.string :description
      t.string :approval

      t.timestamps
    end
  end
end
