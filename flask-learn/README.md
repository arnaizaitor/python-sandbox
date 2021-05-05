# How to run the dockerized Flask app on local

## Build the Docker Image

```docker build -t flask_app .```

## Build and run the docker container

```docker run -p 5000:5000 flask_app```

## Access the app from the browser

Go to ```localhost:5000``` or to ```http://0.0.0.0:5000/``` to access the running flask app