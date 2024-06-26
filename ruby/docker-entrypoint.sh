#!/bin/bash
set -e
# Remove PID
rm -f tmp/pids/server.pid
# Migrations will be run on ALL instances
if [ "${RAILS_DB_MIGRATE_ON_STARTUP}" = "true" ]
then
  bundle exec rails db:migrate
fi
# Call CMD
exec "$@"