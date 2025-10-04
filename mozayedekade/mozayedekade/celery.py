import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mozayedeKade.settings')

app = Celery('mozayedeKade')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()