from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Myuser(models.Model):
    user_type=models.CharField(default='STANDARD', max_length=100)
    account_status=models.CharField(default='ACTIVE', max_length=100)
    date_of_birth=models.DateField()
    whatsapp_enabled_phone_number = models.CharField(max_length=15)
    home_address=models.CharField(max_length=100)
    balance= models.PositiveIntegerField(default=0)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'myusers'

    def __str__(self):
        return f"User: {self.owner}. Balance: {self.balance}"
