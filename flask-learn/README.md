# How to run the dockerized Flask app on local

1. Build the Docker Image:

```docker build -t flask_app .```

2. Build and run the docker container:

```docker run -p 5000:5000 flask_app```

3. Access the app from the browser:

Go to ```localhost:5000``` or to ```http://0.0.0.0:5000/``` to access the running flask app

# How to run the Flask app on local without launching the Docker container

1. Export the ```FLASK_APP``` environment variable as ```export FLASK_APP=app.py```

2. Run the Flask server as ```flask run```

3. Access the app from the browser:

Go to ```localhost:5000``` or to ```http://0.0.0.0:5000/``` to access the running flask app