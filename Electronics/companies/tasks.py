from Electronics.celery import app
import random
from .models import Company
from django.db.models import F

from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@app.task
def increase_debt():
    price = random.randint(5, 500)
    Company.objects.all().update(arrears=F("arrears") + price)
    logger.info(f"ncrease {price}")


@app.task
def reduce_debt():
    price = random.randint(100, 200)
    Company.objects.filter(arrears__gt=price).update(arrears=F("arrears") - price)
    Company.objects.filter(arrears__lt=price).update(arrears=0)
    logger.info(f"reduce {price}")


@app.task(bind=True)
def clear_debt(self, company_id):
    company = Company.objects.get(id=company_id)
    company.arrears = 0
    company.save()
    logger.info(f"clear company arrears {company}")
