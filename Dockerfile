FROM python:3.7-alpine
MAINTAINER Sourabh
ENV PYTHONUNBUFFERED 1  #SETTING THE ENVIRONMENT PYTHON AS UBUFFERED WHICH IS IDEAL FOR DOCKER

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app/


RUN adduser -D user
USER user
