# frozen_string_literal: true

class HomeController < ApplicationController
  def index
    @propositions_by_party = DeputiesProposition.from('deputies AS d')
                                   .joins('JOIN public.deputies_propositions p ON d.id = p.deputy_id')
                                   .group('d.party_initials')
                                   .select('d.party_initials, COUNT(*) AS proposition_count')  end
end
