FROM python:latest

ADD . /mercado_libre_api

WORKDIR /mercado_libre_api

RUN pip install -r requirements.txt

CMD ["python", "server.py"]