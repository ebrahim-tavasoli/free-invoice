#!/bin/sh

python manage.py compilemessages
python manage.py collectstatic --noinput

/bin/sh ./wait-for.sh db:5432 -- python manage.py migrate
DJANGO_SUPERUSER_PASSWORD=admin python manage.py createsuperuser --username admin --email admin@admin.com --noinput

gunicorn -w 1 --bind 0.0.0.0:80 free_invoice.wsgi
