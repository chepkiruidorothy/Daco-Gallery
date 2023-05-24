from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
# Create your models here.

from imageService.resize import resize_image

class Post(models.Model):
    title=models.CharField(max_length=150,unique=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, null = True, blank = True)
    body = RichTextField()
    image = models.ImageField(upload_to="images", blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.image = resize_image(self.image,80)
		#normal save
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = RichTextField(max_length=1000)

    created_on = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
