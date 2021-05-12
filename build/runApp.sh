#!/bin/bash

cd ../web-bundle
npm run build


cd ../web-app
source env/bin/activate
python wsgi.py runserver
