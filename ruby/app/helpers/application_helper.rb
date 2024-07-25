module ApplicationHelper
  include Heroicon::Engine.helpers


  def field_error_message(object, attribute, custom_css_class = "text-rose-600")
    error_messages = object&.errors&.full_messages_for(attribute)
    return ''.html_safe if error_messages.blank?
    error_message = error_messages.first.gsub("#{attribute.to_s.humanize} ", "")
    "<p class=\"#{custom_css_class}\">#{error_message}</p>".html_safe
    end
end
