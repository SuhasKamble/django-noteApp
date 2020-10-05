from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=300)
    msg = models.TextField()
    slug = models.CharField(max_length=255)
    img_url = models.CharField(max_length=3056)
