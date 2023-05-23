from django.contrib import admin

from CMS.models import CharField, ImageField, RichTextField, TextField

# Register your models here.
admin.site.register(CharField)
admin.site.register(TextField)
admin.site.register(RichTextField)
admin.site.register(ImageField)