# frozen_string_literal: true

class ThemesController < ApplicationController
  private

  def themes_params
    params.require(:themes).map do |theme|
      theme.permit(:proposition_id, :theme)
    end
  end
end