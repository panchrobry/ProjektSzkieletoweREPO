
FROM python:3.6


ENV PYTHONUNBUFFERED 1


RUN mkdir /eastrobo1_service


WORKDIR /eastrobo1_service

ADD . /eastrobo1_service/

RUN pip install -r requirements.txt
