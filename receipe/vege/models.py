from django.db import models
class Receipe(models.Model):
    receipe_name=models.TextField(max_length=250)
    receipe_desc=models.TextField()
    receipe_image=models.ImageField(upload_to='photo')
# Create your models here.
