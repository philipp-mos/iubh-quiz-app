#!/bin/bash

cd ../web-app

if [ -d "env" ]
then
    source env/bin/activate
else
    python3 -m venv env
    source env/bin/activate
fi

export LDFLAGS=-L/usr/local/opt/openssl/lib
export CPPFLAGS=-I/usr/local/opt/openssl/include

pip install -r requirements.txt


cd ../web-bundle
npm install
npm run dev:build
