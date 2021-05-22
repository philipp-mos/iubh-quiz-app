# Setup Local Docker Environment
Install Docker-Desktop https://www.docker.com/products/docker-desktop


## Adjust the Configuration Source Class
Update the Configuration-Source-Class from "config.ConfigLocal" to "config.ConfigDocker" in web-app/src/__init__.py

## Start
```
docker-compose up
```
Default binding: 127.0.0.1:5000

## Stop
This shuts down / remove the Containers and remove the network
```
docker-compose down
```

