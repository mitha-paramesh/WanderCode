from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name_t = models.CharField(max_length=250)
    img_t = models.ImageField(upload_to='pics')
    desc_t = models.TextField()

    def __str__(self):
        return self.name_t
