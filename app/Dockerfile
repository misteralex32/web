FROM python:3.9


WORKDIR /app

RUN apt update
RUN apt install python3 python3-pip -y
RUN pip3 install flask
RUN pip3 install prometheus_flask_exporter
RUN pip3 install prometheus_client

EXPOSE 5000
COPY . /app

CMD python3 app/server.py