class SessionsController < ApplicationController
  def new
    @user = User.new
  end

  def create
    @user = User.find_by(email: params[:user][:email])

    if @user.nil?
      flash.now[:alert] = 'User not found.'
      @user = User.new(email: params[:user][:email])
      render :new
    elsif @user.valid_password?(params[:user][:password])
      sign_in(@user)
      redirect_to root_path, notice: 'Logged in successfully.'
    else
      flash.now[:alert] = 'Invalid email or password.'
      render :new
    end
  end
end
