from django.urls import path, include

from petstagram.pets import views

urlpatterns = [
    # Estos urls estan sin include
    # path('add/', views.add_pet, name='add pet'),
    # path('<str:username>/pet/<slug:pet_name>/', views.show_details_pet, name = 'details pet'),
    # path('<str:username>/pet/<slug:pet_name>/edit/', views.edit_details_pet, name = 'edit pet'),
    # path('<str:username>/pet/<slug:pet_name>/delete/', views.delete_pet, name = 'delete pet'),


    # Estos urls son como de arriba pero con include
    path('add/', views.add_pet, name='add pet'),

    path('<str:username>/pet/', include([
        path ('<slug:pet_name>/', views.show_details_pet, name = 'details pet'),
        path('<slug:pet_name>/edit/', views.edit_details_pet, name = 'edit pet'),
        path('<slug:pet_name>/delete/', views.delete_pet, name = 'delete pet'),
]))
]