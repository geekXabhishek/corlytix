from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)