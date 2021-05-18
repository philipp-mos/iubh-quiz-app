# Setup Python Virtual Environment
These scripts need to be executed inside our /web-app folder.
See [setupDevEnv.sh](../../build/setupDevEnv.sh) for whole installation routine.

## Add new Virtual Environment
Create new Virtual Environment
```
python3 -m venv antenv
```

## Activate new Environment
This activates the environment
```
source antenv/bin/activate
```

## Add required Environment Variables
You need to export these variables in order to install all dependencies
```
export FLASK_ENV='development'
export SECRET_KEY=$(python -c 'import os; print(os.urandom(16))')
export LDFLAGS=-L/usr/local/opt/openssl/lib
export CPPFLAGS=-I/usr/local/opt/openssl/include

export SQLALCHEMY_DATABASE_URI=xyz
```

## Install all Dependencies
```
pip install -r requirements.txt
```