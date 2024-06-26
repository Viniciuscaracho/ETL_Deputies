# frozen_string_literal: true

require 'test_helper'

module Webdrivers
  class Chromedriver
    class << self
      def driver_path
        if System.apple_m1_architecture? || System.platform == 'mac'
          '/usr/local/bin/chromedriver'
        else
          super
        end
      end
    end
  end
end

class ApplicationSystemTestCase < ActionDispatch::SystemTestCase
  driver = :headless_chrome # ENV.fetch('CI', false).present? ? :headless_chrome : :chrome
  driven_by :selenium, using: driver, screen_size: [1400, 1400]
end
