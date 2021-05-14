#!/bin/bash

sqlalchemy_database_uri=

cd ../web-app

if [ -d "env" ]
then
    source env/bin/activate
else
    python3 -m venv env
    source env/bin/activate
fi

export FLASK_ENV='development'

export SECRET_KEY=$(python -c 'import os; print(os.urandom(16))')

export LDFLAGS=-L/usr/local/opt/openssl/lib
export CPPFLAGS=-I/usr/local/opt/openssl/include

export SQLALCHEMY_DATABASE_URI=$sqlalchemy_database_uri


pip install -r requirements.txt



cd ../web-bundle
npm install
npm run dev:build
