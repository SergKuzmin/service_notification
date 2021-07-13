
# Start server
    cd proj
    PYTHONPATH=./.. python manage.py migrate
    PYTHONPATH=./.. python manage.py createsuperuser
    PYTHONPATH=./.. python manage.py runserver

# Start worker
    celery -A proj  worker --loglevel=info