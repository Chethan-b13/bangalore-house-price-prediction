web: python manage.py runserver 0.0.0.0:$PORT
web: gunicorn bglrhouseprice.wsgi
release: python manage.py migrate