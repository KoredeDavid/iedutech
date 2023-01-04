web: gunicorn edutech.wsgi --log-file -
release: python manage.py migrate
release: python manage.py collectstatic --no-input