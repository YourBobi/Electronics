from Electronics import settings
from Electronics.celery import app
from companies.models import Company
from django.db.models import F

# from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from django.core.mail import send_mail, message, EmailMessage
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO

logger = get_task_logger(__name__)


@app.task
def send_company_qr_email(company_id, user_email):
    data = Company.objects.get(pk=company_id)
    # create image from company
    qrcode_img = qrcode.make(data)
    canvas = Image.new("RGB", (qrcode_img.pixel_size, qrcode_img.pixel_size), "white")
    canvas.paste(qrcode_img)
    buffer = BytesIO()
    canvas.save(buffer, "PNG")
    # send message
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
