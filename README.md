<img src="./.github/documentation/images/readme_title.png" style="width: 100%;">


| CI.Web-App | CI.Web-Bundle | CD.Staging |
| :--- | :--- | :--- |
| [![Build Status](https://dev.azure.com/philipp-c-moser/IUBH-Quiz-App/_apis/build/status/CI/CI.Web-App?branchName=main)](https://dev.azure.com/philipp-c-moser/IUBH-Quiz-App/_build/latest?definitionId=64&branchName=main) | [![Build Status](https://dev.azure.com/philipp-c-moser/IUBH-Quiz-App/_apis/build/status/CI/CI.Web-Bundle?branchName=main)](https://dev.azure.com/philipp-c-moser/IUBH-Quiz-App/_build/latest?definitionId=65&branchName=main) | |

---

## Python Naming Conventions
See [Python Naming Conventions](.github/documentation/python-naming-conventions.md)

---

## Setup Development Environment
See [Setup Python Virtual Environment](.github/documentation/python-venv-setup.md)

---

## Python Scripts
Requires current location in /web-app and virtual environment set up
### Start Application
workers = number of cores
```
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app
```

### Migrate / Update Database
```
python wsgi.py db upgrade
```

### Generate new Migration
```
python wsgi.py db migrate -m "Migration xyz"
```

---

## NPM Scripts
### Install
```
npm install
```

### Build
```
npm run dev:build
```