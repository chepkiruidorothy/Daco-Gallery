from multiprocessing.sharedctypes import Value
from pyexpat import model
from django.db import models

from ckeditor.fields import RichTextField
from imageService.resize import resize_image

# Create your models here.
class Field(models.Model):
    name = models.CharField(unique=True,max_length=100)

    def __str__(self):
        return self.name

class CharField(Field):
    value = models.CharField(max_length=200)


class TextField(Field):
    value = models.CharField(max_length=1000)

class RichTextField(Field):
    value = RichTextField()


class ImageField(Field):
    value = models.ImageField(upload_to="images")

    def save(self, *args, **kwargs):
        self.value = resize_image(self.value, 99)              
        super(ImageField, self).save(*args, **kwargs)
