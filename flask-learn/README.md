![docker-python-api-1024x533](https://user-images.githubusercontent.com/38442315/117200783-2b94ef00-adec-11eb-866c-f9791c3c5a91.jpg)

# How to run the dockerized Flask app on local

1. Build the Docker Image:

```docker build -t flask_app .```

2. Build and run the docker container:

```docker run -p 5000:5000 flask_app```

3. Access the app from the browser:

Go to ```localhost:5000``` or to ```http://0.0.0.0:5000/``` to access the running flask app.

# How to run the Flask app on local without launching the Docker container

0. Meet all the Python libraries requirements inside ```requirements.txt```.

1. Export the ```FLASK_APP``` environment variable as ```export FLASK_APP=app.py```.

2. Run the Flask server as ```flask run``` or as ```flask run --port 5000``` if you want to specify the port manually.

3. Access the app from the browser:

Go to ```localhost:5000``` or to ```http://0.0.0.0:5000/``` to access the running flask app.

# How to run the Flask app on local on debug mode

The debug mode is very useful while we are developing, because each time we make a change to our code, the server will restart without needing us to restart it manually.

Apart from all the steps above to launch the Flask server manually, before executing the step **2**, we will need to set the environment variable ```FLASK_ENV``` into **development** as it follows: ```export FLASK_ENV="development"```.
