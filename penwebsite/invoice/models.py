from django.db import models

# Create your models here.

class content(models.Model):

    pen_name=models.CharField(max_length=100)
    img1= models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')
    pen_price=models.IntegerField()



