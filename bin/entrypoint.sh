#!/usr/bin/env bash

set -eux

# Migrate database
python site/manage.py migrate

# Collect staticfiles to S3
python site/manage.py collectstatic --noinput --ignore *.scss

# Run server
exec gunicorn site_settings.wsgi \
    --log-file - \
    --log-level debug \
    --pythonpath './site' \
    --workers 2 \
    --bind 0.0.0.0:8080
