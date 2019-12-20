# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cec.settings')

from django.conf import settings

app = Celery('proj')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.update(
        BROKER_URL = 'redis://localhost:6379/0',
        )