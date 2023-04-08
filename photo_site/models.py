from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 20)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Shoot(models.Model):
    person = models.CharField(max_length = 20)

    def __str__(self):
        return self.person

class Gallery(models.Model):
    image = models.ImageField(upload_to="images", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    shoot = models.ForeignKey(Shoot, on_delete = models.CASCADE, null="True")

    # def __str__(self):
    #     return self.category
