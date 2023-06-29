from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
from imageService.resize import resize_image,get_dominantcolor


class Category(models.Model):
	TYPE_CHOICES = (
		('video', 'Video'),
		('photo', 'Photo'),
	)
	name = models.CharField(max_length=20)
	slug = models.SlugField(max_length=100, unique=True, null=True)
	type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='photo')

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
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	shoot = models.ForeignKey(Shoot, on_delete=models.CASCADE, null=True)
	dominant_color = models.CharField(default='(228, 237, 230)', max_length=20)
	height = models.IntegerField(default=200)
	width = models.IntegerField(default=200)
	featured = models.BooleanField(default=False)

	embedded_video = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to="images", blank=True, null=True)

	def clean(self):
		if self.embedded_video and self.image:
			raise ValidationError("Only one of 'embedded_video' or 'image' can be set.")

	def save(self, *args, **kwargs):
		self.clean()
		if not self.image and not self.embedded_video:
			raise ValidationError("Either 'image' or 'embedded_video' must be set.")

		if self.image:
			self.image = resize_image(self.image, 80)
			self.dominant_color = get_dominant_color(self.image)
			self.height = self.image.height
			self.width = self.image.width

		super(Gallery, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		if self.image:
			# Delete the image file when the model instance is deleted
			if os.path.exists(self.image.path):
				os.remove(self.image.path)

		super(Gallery, self).delete(*args, **kwargs)
