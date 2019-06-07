
FROM python:3.6

ENV PYTHONUNBUFFERED 1


RUN mkdir /eastROBO_service


WORKDIR /eastROBO_service


ADD . /eastROBO_service/


RUN pip install -r requirements.txt
