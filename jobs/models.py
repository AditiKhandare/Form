from django.db import models
from django.db.models.fields import CharField, FilePathField
import os
import datetime
from PIL import Image

# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('media', filename)


class Entry(models.Model):

    name = models.CharField(max_length=100)
    number = models.CharField(max_length=12)
    address = models.CharField(max_length=400)
    image=models.ImageField(upload_to=1, null=True, blank=True)
    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path) # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path
    
    class Meta:
        db_table = "entrys"