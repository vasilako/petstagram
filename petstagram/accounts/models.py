from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

LIMIT_LENGHT_NAME = 3
def custom_min_length_validator(value):
    if len(value) < LIMIT_LENGHT_NAME:
        raise ValidationError(
            f'Soy custom validator -> El nombre: "{value}" debe ser al menos {LIMIT_LENGHT_NAME}')
def only_alpha_validadtor(value):
    if not value.isalpha():
        raise ValidationError(
            f'El nombre "{value}" debe ser solo compuestos de letras'
        )
class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    CHOISES = [
        (MALE, 'Male'),
        (FEMALE,'Female'),
        (OTHER, 'Do not show'),
    ]



    username = models.CharField(max_length=30, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)


    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators= [
            MinLengthValidator(
                limit_value=LIMIT_LENGHT_NAME,
                message=f'Soy MinLengthValidator -> El nombre debe ser al menos {LIMIT_LENGHT_NAME}'
            ),
            only_alpha_validadtor
        ]
    )


    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators= [
            custom_min_length_validator,
            only_alpha_validadtor,
        ]
    )
    profile_picture = models.URLField(max_length=200)
    gender = models.CharField(
        max_length=1,
        choices=CHOISES)



    def __str__(self):
        return f'{self.first_name} {self.last_name}'
