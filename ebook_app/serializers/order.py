from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from django.core.mail import send_mail
from django.conf import settings

from ebook_app.models import Book, Order

class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'book', 'customer', 'quantity', 'created_at', 'total_price', 'phone_number', 'is_paid']


    def get_total_price(self, obj):
        return obj.book.price * obj.quantity

    def validate_quantity(self, value):
        try:
            # Fetch the product instance from the database
            book_id = self.initial_data['book']
            book = Book.objects.get(id=book_id)

            # Check the stock
            if value > book.stock:
                raise serializers.ValidationError("Not enough items in stock.")

            if value < 1:
                raise serializers.ValidationError("Quantity must be at least 1.")

            return value

        except ObjectDoesNotExist:
            raise serializers.ValidationError("Book does not exist")


    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        book = order.book
        book.stock -= order.quantity
        book.save()
        self.send_confirmation_email(order)
        return order

    def send_confirmation_email(self, order):
        subject = f"Book Confirmation - {order.id}"
        message = (
            f"Dear {order.customer}, \n\n"
            f"Thank you for your order!\n"
            f"Order ID: {order.id}\n"
            f"Ordered Book:{order.book.name}\n"
            f"Quantity: {order.quantity}\n"
            f"Total price: ${order.book.price*order.quantity}\n\n"
            f"We will process your order soon\n"
            f"Best regards\n"
            f"Your Store team :))"
        )
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [order.customer_email],
            fail_silently=False
        )