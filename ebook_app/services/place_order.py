from django.core.exceptions import ValidationError
from ebook_app.models import Order


def place_order(book, customer, quantity):
    if book and customer and quantity > 0:
        order = Order(book=book, customer=customer, quantity=quantity)
        order.save()
        return order
    else:
        raise ValidationError("Invalid order parameters.")
