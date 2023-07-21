import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ugrainfo.settings.base')

app = Celery('ugrainfo')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'spam_every-10-minutes': {
        'task': 'newsletter.tasks.mail_scheduler',
        'schedule': crontab(minute='0',
                            hour='17')
    },
    'check_expiretime_for_ads': {
        'task': 'snippets.tasks.delete_old_ads',
        'schedule': crontab(
            minute='*/1'
        ),
    }
}
