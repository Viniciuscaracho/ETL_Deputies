class UsersController < ApplicationController
  def index
    @users = User.all
  end
  def edit
    @user = User.find(params[:id])
  end

  def update
    @user = User.find(params[:id])
    if @user.update(user_params)
      redirect_to @user
    else
      flash.now[:alert] = @user.errors.full_messages.join(", ")
    end
  end

  def delete
    @user = User.find(params[:id])
    if @user.destroy
      redirect_to user_url
    end
  end
  def show
    @user = User.find(params[:id])
  end
end