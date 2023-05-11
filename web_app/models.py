from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField 

class blog(models.Model):
    tittle = models.CharField(max_length=222)
    image = CloudinaryField('image')
    description = models.TextField()
    created_by = models.CharField(max_length=222)

    def __str__(self):
        return self.tittle

class contactus(models.Model):
    name = models.CharField(max_length=222)
    email = models.EmailField()
    mobile = models.IntegerField()
    address = models.CharField(max_length=222)
    subject = RichTextField()

    def __str__(self):
        return self.name

class profile(models.Model):
    image = CloudinaryField('image')
    user = models.CharField(max_length=222)

    def __str__(self):
        return self.user

class leavecomment(models.Model):
    adds_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    comment = models.CharField(max_length=400)
    
    def __str__(self) -> str:
        return self.adds_id
    









# Create your models here.
