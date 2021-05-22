#!/bin/bash

sqlalchemy_database_uri=

cd ../web-app

if [ -d "antenv" ]
then
    source antenv/bin/activate
else
    python3 -m venv antenv
    source antenv/bin/activate
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
