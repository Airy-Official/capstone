from django.db import models
import datetime
import os



# Create your models here.
class Student(models.Model):
    sid = models.CharField(max_length=4)
    sname = models.CharField(max_length=255)
    scontact = models.CharField(max_length=15)

    def __str__(self):
        return self.sname

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s", (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Destination(models.Model):

    name = models.TextField(max_length=100)
    img = models.ImageField(upload_to=filepath, null=True, blank=True)
    desc = models.TextField(max_length=500, null=True)
    price = models.TextField(max_length=50, null=True)
