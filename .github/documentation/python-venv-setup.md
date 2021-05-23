# Setup Python Virtual Environment
These scripts need to be executed inside our /web-app folder.
See [setupDevEnv.sh](../../build/setupDevEnv.sh) for whole installation routine.

## Add new Virtual Environment
Create new Virtual Environment
```
python3 -m venv env
```

## Activate new Environment
This activates the environment
```
source env/bin/activate
```

## Add required Environment Variables
You need to export these variables in order to install all dependencies
```
export LDFLAGS=-L/usr/local/opt/openssl/lib
export CPPFLAGS=-I/usr/local/opt/openssl/include
```

## Install all Dependencies
```
pip install -r requirements.txt
```

## Setup Application Environment-Variables
In web-app Folder you will find our *.env.example* File. You need to copy it and save it as *.env*. Now update the Variables with your values.