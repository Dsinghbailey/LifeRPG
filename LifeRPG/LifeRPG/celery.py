from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
# from AdminApp.tasks import rec_user_missions

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LifeRPG.settings')

app = Celery('LifeRPG')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(30.0,
#                              rec_user_missions.s(),
#                              name='add every 30')


@app.task
def test(arg):
    print(arg)
