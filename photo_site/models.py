from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
from imageService.resize import resize_image,get_dominantcolor

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
	shoot = models.ForeignKey(Shoot, on_delete = models.CASCADE, null=True)
	dominant_color = models.CharField(default='(228, 237, 230)',max_length=20)
	height = models.IntegerField(default=200)
	width = models.IntegerField(default=200)


	def save(self, *args, **kwargs):   
		self.image = resize_image(self.image)
		self.dominant_color = get_dominantcolor(self.image)
		self.height = self.image.height
		self.width = self.image.width
		#normal save
		super(Gallery, self).save(*args, **kwargs)#normal save