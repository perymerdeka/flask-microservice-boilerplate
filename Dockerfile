FROM library/python:3.9.10-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# PDFTK Setup
RUN apt update -y

RUN mkdir /app

RUN ls /app
WORKDIR /app

RUN pip install --upgrade pip
ADD requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir

ADD . /app/