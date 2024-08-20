# frozen_string_literal: true


class SearchController < ApplicationController
  before_action :authenticate_user!

  def index
    if params[:query].present?
      @deputies = Deputy.search_by_name_and_party(params[:query]).paginate(page: params[:page], per_page: 10)
    else
      @deputies = Deputy.distinct.paginate(page: params[:page], per_page: 10)
    end
  end

  def show
    @deputy = Deputy.find(params[:id])
  end
end
