from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_agregator.settings')
app = Celery('news_agregator')
app.conf.timezone = 'UTC'
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
