# frozen_string_literal: true

ENV['RAILS_ENV'] ||= 'test'
require_relative "../config/environment"
require "rails/test_help"

module ActiveSupport
  class TestCase
    # Run tests in parallel with specified workers
    parallelize(workers: :number_of_processors)

    include Devise::Test::IntegrationHelpers
    include ActionCable::TestHelper
    include ActionMailer::TestHelper

    # Setup all fixtures in test/fixtures/*.yml for all tests in alphabetical order.
    fixtures :all

    def register_user(**kwargs)
      User.create!(
        username: kwargs.fetch(:username, Faker::Name.name),
        email: kwargs.fetch(:email, Faker::Internet.email),
        password: kwargs.fetch(:password, 'password'),
        password_confirmation: kwargs.fetch(:password_confirmation, 'password')
      )
    end

    def sign_in(resource, scope: nil)
      scope ||= Devise::Mapping.find_scope!(resource)
      login_as(resource, scope: scope)
    end
  end
end
