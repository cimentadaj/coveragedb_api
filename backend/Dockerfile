FROM python:3.10.0-slim-buster

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql libpq-dev \
    && apt-get clean

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN pip install --upgrade pip
COPY ./requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt

COPY . /backend/
