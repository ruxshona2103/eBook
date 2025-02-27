import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_telegram_notification
from .models import Order

@receiver(post_save, sender=Order)
def notify_admin(sender, instance, created, **kwargs):
    if created:
        send_telegram_notification.delay(
            order_id = instance.id,
            book_name = instance.book.name,
            quantity=instance.quantity,
            customer_username=instance.customer.username,
            phone_number=instance.phone_number
        )