FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y gettext netcat
COPY ./invoice_creator .
RUN pip install -r requirements.txt
RUN pip install gunicorn

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
