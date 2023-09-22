from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
  
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
            super(Product, self).save(*args, **kwargs)
