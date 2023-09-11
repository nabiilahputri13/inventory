from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
  
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
            super(Product, self).save(*args, **kwargs)
