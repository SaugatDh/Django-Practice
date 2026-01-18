from django.db import models
from django.conf import settings

# Create your models here.
class MilkOrder(models.Model):
    MILK_CHOICES = [
        ('cow','Cow Milk'),
        ('buffalo','Buffalo Milk'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="milk_orders")
    milk_type = models.CharField(max_length=10,choices = MILK_CHOICES)
    quantity = models.DecimalField(max_digits=4,decimal_places=1,help_text="Quantity in liters")
    order_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"{self.milk_type} - {self.quantity} L"

    