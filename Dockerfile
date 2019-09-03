FROM python:3.7-alpine
WORKDIR /usr/src/
COPY ./requirements.txt /usr/src/
RUN pip install -r requirements.txt
COPY . .
