# frozen_string_literal: true

class DeputiesController < ApplicationController
  def show
    @deputy = Deputy.find(params[:id])
    @proposition = @deputy.propositions
  end


  private

  def deputies_params
    params.require(:deputies).map do |deputy|
      deputy.permit(:id, :civil_name, :party_initials, :proposition_id)
    end
  end
end
