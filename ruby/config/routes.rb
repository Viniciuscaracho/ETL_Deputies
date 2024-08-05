Rails.application.routes.draw do
  devise_for :users, controllers: { registrations: 'registrations', sessions: 'sessions' }
  resources :users, only: [:index, :show]
  root 'home#index'
  resources :search
  resources :deputies
  resources :propositions
  resources :themes
  resources :votes
end
