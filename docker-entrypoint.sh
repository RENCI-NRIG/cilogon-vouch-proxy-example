#!/usr/bin/env bash

cd /
virtualenv -p /usr/local/bin/python venv
source venv/bin/activate
pip install -r requirements.txt

if [[ "$1" == 'run_server' ]]; then
  export FLASK_APP=/code/app.py
  python -m flask run --host 0.0.0.0 --port 5000
else
  exec "$@"
fi
