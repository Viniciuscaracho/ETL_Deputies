# frozen_string_literal: true

class PropositionsController < ApplicationController
  def index
    @propositions = Proposition.find(params[:id])
  end


  private
  def propositions_params
    params.require(:propositions).map do |proposition|
      proposition.permit(:id, :type, :summary)
    end
  end
end
