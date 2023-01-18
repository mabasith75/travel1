from django.db import models

# Create your models here.
class lugar(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='imagenes')
    desc = models.TextField()

    def __str__(self):
        return self.name

class team(models.Model):
    img = models.ImageField(upload_to='imagenes2')
    nombre = models.CharField(max_length=250)
    sobre = models.TextField()

    def __str__(self):
        return self.nombre

