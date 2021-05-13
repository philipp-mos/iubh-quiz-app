#!/bin/bash

secret_key=
sqlalchemy_database_uri=


cd ../web-app

if [ -d "env" ]
then
    source env/bin/activate
else
    python3 -m venv env
    source env/bin/activate
fi

export FLASK_ENV=development

export SECRET_KEY=$secret_key
export SQLALCHEMY_DATABASE_URI=$sqlalchemy_database_uri

export LDFLAGS=-L/usr/local/opt/openssl/lib
export CPPFLAGS=-I/usr/local/opt/openssl/include

pip install -r requirements.txt



cd ../web-bundle
npm install
npm run dev:build