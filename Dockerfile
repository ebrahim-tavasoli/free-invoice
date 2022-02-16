FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y gettext netcat
COPY ./free_invoice .
RUN pip install -r requirements.txt
RUN pip install gunicorn

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
