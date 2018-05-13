#!/usr/bin/env bash

npm run prod
./manage.py migrate --settings=ldlights.settings.prod
./manage.py collectstatic --settings=ldlights.settings.prod --noinput
uwsgi --ini uwsgi.ini
