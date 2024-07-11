# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.1].define(version: 2024_07_11_131925) do
  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "deputies", force: :cascade do |t|
    t.string "name"
    t.string "party"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "proposition_authors", force: :cascade do |t|
    t.bigint "deputy_id", null: false
    t.bigint "proposition_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["deputy_id"], name: "index_proposition_authors_on_deputy_id"
    t.index ["proposition_id"], name: "index_proposition_authors_on_proposition_id"
  end

  create_table "proposition_themes", force: :cascade do |t|
    t.bigint "proposition_id", null: false
    t.bigint "theme_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["proposition_id"], name: "index_proposition_themes_on_proposition_id"
    t.index ["theme_id"], name: "index_proposition_themes_on_theme_id"
  end

  create_table "propositions", force: :cascade do |t|
    t.text "description"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "themes", force: :cascade do |t|
    t.string "theme"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "users", force: :cascade do |t|
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "username"
    t.string "password_digest"
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
  end

  create_table "votes", force: :cascade do |t|
    t.bigint "proposition_id", null: false
    t.string "vote"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["proposition_id"], name: "index_votes_on_proposition_id"
  end

  add_foreign_key "proposition_authors", "deputies"
  add_foreign_key "proposition_authors", "propositions"
  add_foreign_key "proposition_themes", "propositions"
  add_foreign_key "proposition_themes", "themes"
  add_foreign_key "votes", "propositions"
end
