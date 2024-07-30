# frozen_string_literal: true

class DeputiesController < ApplicationController
  def show
    @deputies = Deputy.find(params[:id])
    @propositions = Proposition.find(params[:id])
    @themes = Theme.find(params[:proposition_id])
    @votes = Vote.find(params[:proposition_id])
  end
end
