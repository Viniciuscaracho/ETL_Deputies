# frozen_string_literal: true


class HomeController < ApplicationController
  def index
    if params[:query].present?
      @deputies = Deputy.search_by_name_and_party(params[:query]).distinct.paginate(page: params[:page], per_page: 5)
    else
      @deputies = Deputy.distinct.paginate(page: params[:page], per_page: 5)
    end
  end

  def show
    @deputy = Deputy.find(params[:id])
  end
end
