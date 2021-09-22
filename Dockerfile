# imagem base
FROM python:3.9.4

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN apt update \
    && apt install -y libpq-dev gcc

RUN pip install psycopg2
