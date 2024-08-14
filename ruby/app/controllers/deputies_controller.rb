# frozen_string_literal: true

class DeputiesController < ApplicationController
  def show
    @deputy = Deputy.find(params[:id])
    if params[:query].present?
      @propositions = @deputy.propositions.paginate(page: params[:page], per_page: 10)
    else
      @propositions = @deputy.propositions.distinct.paginate(page: params[:page], per_page: 10)
    end
  end

  private

  def deputies_params
    params.require(:deputies).map do |deputy|
      deputy.permit(:id, :civil_name, :party_initials, :proposition_id)
    end
  end
end