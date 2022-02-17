from django.db import models

# Create your models here.


class Fish(models.Model):
    description = models.TextField(max_length=300)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.description}'
