# frozen_string_literal: true

class DeputiesController < ApplicationController
  def show
    @deputies = Deputy.find(params[:id])

  end
end
