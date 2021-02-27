from django.db import models

# Create your models here.on

class Contactpage(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.TextField()
    message = models.TextField()

class Pagecontact(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.TextField()
    message = models.TextField()

# From here i commented because not pushing to database disabled
# class Letterhead_Generator(models.Model):
#     business = models.CharField(max_length=30, blank=True)
#     tagline = models.CharField(max_length=50, blank=True)
#     message1 = models.CharField(max_length=100, blank=True)
#     email = models.EmailField(max_length=254, blank=True)
#     website = models.URLField(default='')
#     image_upload = models.ImageField(upload_to='images/')

class Uploaded_Images(models.Model):
    image_upload = models.ImageField(upload_to='images/')
