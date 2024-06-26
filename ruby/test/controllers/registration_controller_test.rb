require 'test_helper'
class RegistrationControllerTest < ApplicationController
  def setup
    @user = register_user(
      username: "Aubrey Fahey PhD",
      email: "jerrell.rogahn@dooley.example",
      password: "password",
      password_confirmation: "password"
    )
  end

  test "should create user" do
    post registrations_url(@url), params: {
      user: {
        username: @user.username,
        email: @user.email,
        password: @user.password,
        password_confirmation: @user.password
      }
    }

    assert_response :redirect
    follow_redirect!
    assert_response :success
  end
end