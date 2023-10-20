from Electronics import settings
from Electronics.celery import app
from companies.models import Company

from celery.utils.log import get_task_logger
from django.core.mail import EmailMessage
import qrcode
from PIL import Image
from io import BytesIO

logger = get_task_logger(__name__)


@app.task
def send_company_qr_email(company_id, user_email):
    """Отправка QR на почту.

    Данные преобразуются в QR с помощью библиотеки qrcode. QR переводится PIL.Image и
    сохраняется в BytesIO буфер. При отправке сообщения данные берутся из него и преобразуются в .png.

    Parameters
    ----------
    company_id : int
        id компании для отправки

    user_email : str
        почта на которую нужно отправить QR
    """
    data = Company.objects.get(pk=company_id)
    # создание qr
    qrcode_img = qrcode.make(data)
    canvas = Image.new("RGB", (qrcode_img.pixel_size, qrcode_img.pixel_size), "white")
    canvas.paste(qrcode_img)
    buffer = BytesIO()
    canvas.save(buffer, "PNG")
    # отправка сообщения
    qr_message = EmailMessage(
        "Store information",
        str(data),
        settings.EMAIL_HOST_USER,
        [user_email],
    )
    qr_message.content_subtype = "png"
    qr_message.attach("data.png", buffer.getvalue(), "file/png")
    qr_message.send()

    logger.info("Email sent")
