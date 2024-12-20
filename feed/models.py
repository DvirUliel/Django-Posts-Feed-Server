from django.db import models
from sorl.thumbnail import ImageField

class Post(models.Model):
    title = models.CharField(max_length=140)
    image = ImageField()

    def __str__(self):
        return self.title