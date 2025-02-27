from django.db import  models
from .book import  Book
from django.core.validators import RegexValidator


from django.contrib.auth import get_user_model
User = get_user_model()

phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Phone number must be in the format: '+998xxxxxxx'."
)

class Order(models.Model):
    PENDING = 'Pending',
    PROCESSING = 'Processing',
    SHIPPED = 'Shipped',
    DELIVERED = 'Delivered',
    CANCELED = 'Canceled'

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=False, null=False)
    is_paid = models.BooleanField(default=False, null=True)
    customer_email = models.EmailField()

    def set_statuc(self, new_status):
        if new_status not in dict(self.STATUS_CHOICES):
            raise ValueError("invalid choice")
        self.status = new_status
        self.save()


    def is_transition_allowed(self, new_status):
        allowed_transitions = {
            self.PENDING: [self.PROCESSING, self.CANCELED],
            self.PROCESSING:[self.SHIPPED, self.CANCELED],
            self.SHIPPED: [self.DELIVERED, self.CANCELED],
        }

        return new_status in allowed_transitions.get(self.status, [])

    def __str__(self):
        return f"Ordered {self.book.name} by {self.customer.name}"
