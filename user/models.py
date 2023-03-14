from django.db import models
import uuid
from django.contrib.auth.models import User
import secrets
from .paystack import Paystack

# Create your models here.

class Payment(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
     amount = models.PositiveIntegerField()
     ref = models.CharField(max_length=199)
     email = models.EmailField()
     verified = models.BooleanField(default=False)
     queried = models.BooleanField(default=False)
     date_created = models.DateTimeField(auto_now_add=True)
     
     class Meta:
        ordering = ('-date_created',)

     def __str__(self):
        return f"Payment: {self.amount}, Verified: {self.verified}, queried: {self.queried}"

     def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref

        super().save(*args, **kwargs)

     def amount_value(self):
        return int(self.amount) * 100

     def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False
    
class Cabservice(models.Model):
    name=models.CharField(max_length=99)
    def __str__(self):
        return self.name

TYPE=(
    (1, 'Renew Subscription'),
    (2, 'Change Subscription'),
)

class CablePlan(models.Model):
    service = models.ForeignKey(Cabservice, on_delete=models.CASCADE)
    name = models.CharField(max_length=299)
    amount=models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} - #{self.amount}'

class Cable(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, max_length=2)
    queried=models.BooleanField(default=False)
    name=models.CharField(max_length=100, default='Cable TV')
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    card_number=models.CharField(max_length=30)
    status=models.CharField(max_length=100, default='Processing')
    service=models.ForeignKey(Cabservice, on_delete=models.SET_NULL, null=True)
    choose_type=models.IntegerField(choices=TYPE, default=0)
    plan=models.ForeignKey(CablePlan, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    recharge_now=models.BooleanField(default=True)
    schedule_for_later=models.BooleanField(default=False)
    one_off=models.BooleanField(default=True)
    auto_renew=models.BooleanField(default=False)

    def __str__(self):
        return f"Queried: {self.queried} by {self.owner} and {self.status}"

class EduService(models.Model):
    name = models.CharField(max_length=299)
    def __str__(self):
        return self.name

class Checker(models.Model):
    service=models.ForeignKey(EduService, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=299)
    amount=models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} - #{self.amount}'

class Education(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, max_length=2)
    queried=models.BooleanField(default=False)
    name=models.CharField(max_length=100, default='Education')
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=15)
    status=models.CharField(max_length=100, default='Processing')
    service=models.ForeignKey(EduService, on_delete=models.SET_NULL, null=True)
    quantity=models.ForeignKey(Checker, on_delete=models.SET_NULL, null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Queried: {self.queried} by {self.owner} and {self.status}"

class ElectService(models.Model):
    service = models.CharField(max_length=299)
    
    def __str__(self):
        return self.service

class Elect(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, max_length=2)
    queried=models.BooleanField(default=False)
    name=models.CharField(max_length=100, default='Electricity')
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=100, default='Processing')
    service=models.ForeignKey(ElectService, on_delete=models.SET_NULL, null=True)
    meter_number=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=15)
    date=models.DateTimeField(auto_now_add=True)
    amount=models.PositiveIntegerField()
    recharge_now=models.BooleanField(default=True)
    schedule_for_later=models.BooleanField(default=False)
    one_off=models.BooleanField(default=True)
    auto_renew=models.BooleanField(default=False)

    def __str__(self):
        return f"Queried: {self.queried} by {self.owner} and {self.status} for {self.amount}"

class With(models.Model):
    queried=models.BooleanField(default=False)
    amount=models.PositiveIntegerField()
    charge=models.PositiveIntegerField(default=50)
    status=models.CharField(max_length=100, default='Processing')
    date=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Queried: {self.queried} by {self.owner} and {self.status} for {self.amount}"

class Bank(models.Model):   
    default=models.BooleanField(default=False)
    bank_name=models.CharField(max_length=100)
    account_number=models.CharField(max_length=10)
    account_name=models.CharField(max_length=100)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account_number} by {self.owner} and {self.default}"
    
class Service(models.Model):
    service = models.CharField(max_length=99)
    
    def __str__(self):
        return self.service

class Airtime(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, max_length=2)
    queried=models.BooleanField(default=False)
    status=models.CharField(max_length=100, default='Processing')
    choose_network=models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    phone_number=models.CharField(max_length=15)
    amount=models.PositiveIntegerField()
    date=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Queried: {self.queried} by {self.owner} and {self.status}"

class Plan(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    plan = models.CharField(max_length=99)
    amount=models.PositiveIntegerField()

    def __str__(self):
        return f'{self.plan} - #{self.amount}'

AVAIL = (('Poor', 'Poor'),('Excellent', 'Excellent'), ('Unavailable', 'Unavailable'))
    
class Availability(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=99, choices=AVAIL, default='Poor')

class Data(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, max_length=2)
    queried=models.BooleanField(default=False)
    status=models.CharField(max_length=100, default='Processing')
    service=models.ForeignKey(Service, on_delete = models.SET_NULL, null=True)
    plan=models.ForeignKey(Plan, on_delete = models.SET_NULL, null=True)
    phone_number=models.CharField(max_length=15)
    recharge_now=models.BooleanField(default=True)
    schedule_for_later=models.BooleanField(default=False)
    one_off=models.BooleanField(default=True)
    auto_renew=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Queried: {self.queried} by {self.owner} and {self.status}"
