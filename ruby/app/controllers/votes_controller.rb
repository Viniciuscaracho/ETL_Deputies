# frozen_string_literal: true

class VotesController < ApplicationController
  private

  def votes_params
    params.require(:votes).map do |vote|
      vote.permit(:id, :proposition_id, :description, :approval)
    end
  end
end