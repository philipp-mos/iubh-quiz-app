#!/bin/bash

cd ../web-bundle
npm run dev:build


cd ../web-app
source env/bin/activate

gunicorn --workers 4 --bind 0.0.0.0:5000 app:app
# or: python app.py runserver