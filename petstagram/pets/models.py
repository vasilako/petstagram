from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Pet(models.Model):

    name = models.CharField(max_length=30)
    pet_photo = models.URLField()
    birth_date = models.DateField(blank=True, null=True)
    slug = models.SlugField(editable=False, unique=True)

    def __str__(self):
        return f'id {self.id} - name {self.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(f'{self.name}-{self.id}')
        return super().save(*args, **kwargs)

