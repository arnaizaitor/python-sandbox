FROM python:3

WORKDIR /app

EXPOSE 5000
EXPOSE 27017

ENV FLASK_APP=app.py
ENV FLASK_ENV="development"

COPY . /app
RUN pip install -r requirements.txt

ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]