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
    
    def __str__(self):
        return f"{self.milk_type} - {self.quantity} L"
    
    
class OrderAssignment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Assignment'),
        ('on_the_way', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]
    order = models.OneToOneField(MilkOrder,on_delete=models.CASCADE,related_name='assignment')
    staff_member = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,limit_choices_to={'is_staff':True},related_name="tasks")
    status = models.CharField(max_length=20,choices = STATUS_CHOICES,default='pending')
    delivery_notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Assignment for Order #{self.order.id} - {self.status}"
    

    