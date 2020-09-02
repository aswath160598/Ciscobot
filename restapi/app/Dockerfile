FROM python:3.7-slim-buster
LABEL maintainer="png"

WORKDIR /app

RUN pip install flask
RUN pip install flask_restful
RUN pip install configparser
RUN pip install mysql-connector-python


COPY app.py /app
COPY module/holidays.py /app
COPY module/birthday.py /app
COPY module/users.py /app

CMD python app.py
