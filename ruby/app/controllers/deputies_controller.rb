# frozen_string_literal: true

class DeputiesController < ApplicationController
  def index
    @deputies = Deputy.all
  end
  def show
    @deputies = Deputy.find(params[:id])
  end
end
