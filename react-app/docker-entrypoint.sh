#!/usr/bin/env bash

cd /code

if [[ "$1" == 'run_server' ]]; then
  # defaults to running on port 5000
  npm install --silent
  npm run build
  npm install -g serve
  serve -s build
elif [[ "$1" == 'run_dev' ]]; then
  # defaults to running on port 3000
  # requires stdin_open = true (or "-i" in "docker run ..." command)
  npm install --verbose
  npm start
else
  exec "$@"
fi
