from ugrainfo.celery import app
from .models import Advert
import datetime
from celery.schedules import crontab
from django.utils import timezone
from django.db import models




@app.task
def delete_old_ads():
    Advert.filter(expiration_time__lte=datetime.datetime.now()).delete()
