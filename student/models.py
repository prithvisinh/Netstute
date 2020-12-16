from django.db import models
from login.models import Classroom

# Create your models here.
class stupload(models.Model):
    classname = models.CharField(max_length=30)
    filename = models.CharField(max_length=30)
    submission = models.FileField(upload_to='submission/')

    def __str__(self):
        return self.filename

class links(models.Model):
    classname = models.CharField(max_length=30)
    link = models.CharField(max_length=50)