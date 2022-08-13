web: gunicorn polls.wsgi:application --logfile --log-level debug
python manage.py collectstatic --noinput
manage.py migrate