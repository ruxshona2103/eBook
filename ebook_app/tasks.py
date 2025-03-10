import time

import requests
from config.settings import CHAT_ID, TELEGRAM_BOT_TOKEN

from celery import shared_task

@shared_task()
def send_telegram_notification(order_id, book_name, quantity, customer_username, phone_number):
    time.sleep(4)
    token= TELEGRAM_BOT_TOKEN
    method = 'sendMessage'
    message_text = f"New Order : {order_id}\n Book {book_name}\nQuantity:{quantity}\n"\
                    f"Client: {customer_username}\n Phone_number {phone_number}"

    response = requests.post(
        url=f'https://api.telegram.org/bot{token}/{method}',
        data={'chat_id':CHAT_ID, 'text':message_text}
    ).json()




