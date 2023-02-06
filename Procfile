web: gunicorn todo.wsgi --log-file -
web: python manage.py migrate && gunicorn todo.wsgi --log-file -