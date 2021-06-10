<img src="./.github/documentation/images/readme_title.png" style="width: 100%;">


| CI.Web-App | CI.Web-Bundle | CD.IU-Quiz.Staging |
| :--- | :--- | :--- |
| [![Build Status](https://dev.azure.com/philipp-c-moser/IUBH-Quiz-App/_apis/build/status/CI/CI.Web-App?branchName=main)](https://dev.azure.com/philipp-c-moser/IUBH-Quiz-App/_build/latest?definitionId=64&branchName=main) | [![Build Status](https://dev.azure.com/philipp-c-moser/IUBH-Quiz-App/_apis/build/status/CI/CI.Web-Bundle?branchName=main)](https://dev.azure.com/philipp-c-moser/IUBH-Quiz-App/_build/latest?definitionId=65&branchName=main) | [![Build Status](https://dev.azure.com/philipp-c-moser/IUBH-Quiz-App/_apis/build/status/CD/CD.IU-Quiz.Staging?branchName=devops%2FIQA-38-CD-Pipeline)](https://dev.azure.com/philipp-c-moser/IUBH-Quiz-App/_build/latest?definitionId=66&branchName=devops%2FIQA-38-CD-Pipeline) |

---

| Production | Staging |
| :--- | :--- |
| https://iuquiz.azurewebsites.net | https://iuquiz-staging.azurewebsites.net |

---

## Python Naming Conventions
See [Python Naming Conventions](.github/documentation/python-naming-conventions.md)

---

## Setup Development Environment
See [Setup Python Virtual Environment](.github/documentation/python-venv-setup.md)

---

## Use Docker for local Setup
See [Setup Docker](.github/documentation/python-docker-setup.md)

---

## Python Scripts
Requires current location in /web-app and virtual environment set up
### Start Application
To start the application run one of the following commands
```
python app.py runserver -h 0.0.0.0
```
```
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app
```
### Run Unit Tests
Run all Unit Tests in /tests
```
pytest
```

### Migrate / Update Database
```
python app.py db upgrade
```

### Generate new Migration
```
python app.py db migrate -m "Migration xyz"
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