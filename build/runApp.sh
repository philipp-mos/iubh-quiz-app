#!/bin/bash

cd ../web-bundle
npm run dev:build


cd ../web-app
source env/bin/activate
python wsgi.py runserver
