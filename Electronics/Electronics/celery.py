import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Electronics.settings")

app = Celery("Electronics")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.timezone = "Europe/Minsk"


# таски в очередь
app.conf.beat_schedule = {
    "every-3-hours": {
        "task": "companies.tasks.increase_debt",
        "schedule": 3600 * 3,
    },
    "every-morning": {
        "task": "companies.tasks.reduce_debt",
        "schedule": crontab(hour="6", minute="30"),
    },
}
