#text file with commands for assembling the docker image


# pull the official base image (linux light weight os)
FROM python:3.8-slim-buster

#everything will be sent to terminal in order to see some logs

ENV PYTHONBUFFERED=1

# set work directory
WORKDIR /app

#copy requirements

COPY ./requirements.txt requirements.txt

#install requirements

RUN pip3 install -r requirements.txt

#copying all the thing in the folder (no need with docker compose)

#COPY . /app

#running the final comannd (no need with docker compose)

#CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]