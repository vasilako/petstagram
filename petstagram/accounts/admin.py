from django.contrib import admin

from petstagram.accounts.models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # Eso genera las columnas que se listan en el admin
    list_display = [ 'username','first_name', 'last_name', 'gender','email',]

    # Eso limita los campos del formulario admin a la hora de crear el objeto
    # Ojo afecta solo al formulario, si no están todos los campos no se pueden rellenar.
    fields = ('username', 'password', 'email')


