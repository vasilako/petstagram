from django.core.validators import MinLengthValidator
from django.core.validators import validate_image_file_extension
from django.db import models

from petstagram.pets.models import Pet


def file_size_5mb_validator(file):
    from django.core.exceptions import ValidationError
    limit = 5.0 * 1024 * 1024
    if file.size > limit:
        raise ValidationError("El tamaño del archivo supera 5MB")

# Create your models here.
class Photos(models.Model):
    photo =models.ImageField(
        null=False,
        blank=False,
        upload_to= 'pets_photos',
        validators=((file_size_5mb_validator, validate_image_file_extension))
    )

    descrtiption = models.CharField(
        max_length=300,
        validators=[
            MinLengthValidator(
                limit_value=10,
            )
       ]
    )

    location = models.CharField(
        max_length=30,
    )

    tagged_pets = models.ManyToManyField(
        Pet,

    )

    date = models.DateField(
        auto_now=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.photo.name