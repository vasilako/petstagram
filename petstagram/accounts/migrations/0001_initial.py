# Generated by Django 4.1.1 on 2022-11-19 12:10

import django.core.validators
from django.db import migrations, models
import petstagram.accounts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(limit_value=3, message='Soy MinLengthValidator -> El nombre debe ser al menos 3'), petstagram.accounts.models.only_alpha_validadtor])),
                ('last_name', models.CharField(max_length=30, validators=[petstagram.accounts.models.custom_min_length_validator, petstagram.accounts.models.only_alpha_validadtor])),
                ('profile_picture', models.URLField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Do not show')], max_length=1)),
            ],
        ),
    ]
