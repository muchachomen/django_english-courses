from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.TextField()
    author = models.TextField()

    def __str__(self):
        return self.name


class MyModel(models.Model):
    my_file = models.FileField(upload_to='files/')
    my_image = models.ImageField(upload_to='images/')
