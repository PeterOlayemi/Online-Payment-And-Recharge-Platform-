from django.db import models

# Create your models here.

class Image1(models.Model):
    image1 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image2(models.Model):
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image3(models.Model):
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image4(models.Model):
    image4 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image5(models.Model):
    image5 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image8(models.Model):
    image8 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image9(models.Model):
    image9 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image10(models.Model):
    image10 = models.ImageField(upload_to='images/', blank=True, null=True)

class Image20(models.Model):
    image20 = models.ImageField(upload_to='images/', blank=True, null=True)
