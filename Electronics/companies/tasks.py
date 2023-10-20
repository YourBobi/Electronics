from Electronics.celery import app
import random
from .models import Company
from django.db.models import F

from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@app.task
def increase_debt():
    """Метод для увеличения задолженности.

    Метод увеличивает задолженность на рандомное число от 5 до 500.
    """
    price = random.randint(5, 500)
    Company.objects.all().update(arrears=F("arrears") + price)
    logger.info(f"ncrease {price}")


@app.task
def reduce_debt():
    """Метод для уменьшения задолженности.

    Метод уменьшает задолженность на рандомное число от 100 до 200. Если
    задолженность равна 0, то не уменьшает.
    """
    price = random.randint(100, 200)
    Company.objects.filter(arrears__gt=price).update(arrears=F("arrears") - price)
    Company.objects.filter(arrears__lt=price).update(arrears=0)
    logger.info(f"reduce {price}")


@app.task(bind=True)
def clear_debt(self, company_id):
    """Метод для удаления задолженности.

    Очищает задолженность перед поставщиком

    Parameters
    ----------
    company_id : int
        ID компании для очищения
    """
    company = Company.objects.get(id=company_id)
    company.arrears = 0
    company.save()
    logger.info(f"clear company arrears {company}")
