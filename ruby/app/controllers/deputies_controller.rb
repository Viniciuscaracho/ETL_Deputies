# frozen_string_literal: true

class DeputiesController < PropositionsController
  def show
    @deputy = @propositions.deputy_id
  end

  private

  def deputies_params
    params.require(:deputies).map do |deputy|
      deputy.permit(:id, :civil_name, :party_initials, :proposition_id)
    end
  end
end