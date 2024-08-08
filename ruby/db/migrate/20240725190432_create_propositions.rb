class CreatePropositions < ActiveRecord::Migration[7.1]
  def change
    create_table :propositions do |t|
      t.string :type
      t.text :summary
      t.integer :deputy_id
      t.integer :theme_id
      t.integer :vote_id

      t.timestamps
    end
  end
end
