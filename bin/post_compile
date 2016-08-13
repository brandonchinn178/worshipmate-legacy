#!/usr/bin/env bash

# fail entire script if any operation fails
set -eo pipefail

function message {
    echo -e "\n-----> $1"
}

# Automatically migrate when deploying to Heroku
message "Running Django Migrations"
python site/manage.py migrate

message "Compiling staticfiles"
python bin/compile_staticfiles.py
python site/manage.py collectstatic --noinput -i *.scss
