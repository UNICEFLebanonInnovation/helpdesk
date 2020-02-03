web: gunicorn config.wsgi -w 4 -b "0.0.0.0:$PORT" --log-level=info --timeout=3200
worker: celery worker --app=helpdesk.taskapp --loglevel=info
beater: celery beat --app=helpdesk.taskapp --loglevel=info

