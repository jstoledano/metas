FROM python:alpine
MAINTAINER Javier Sanchez <js.toledano@me.com>

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install --upgrade pip \
  && pip install django \
  && pip install psycopg2 \
  && apk del build-deps \
  \
  && pip install -r requirements.txt

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ENV PORT=8000
EXPOSE 8000

# CMD python /app/manage.py runserver 0.0.0.0:$PORT
