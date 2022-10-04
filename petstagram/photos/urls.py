from django.urls import path, include

from petstagram.photos import views

urlpatterns = [
    path('add/', views.add_photo, name = 'add photo'),
    path('<int:pk>/', include([
    path('', views.show_details_photo, name = 'details photo'),
    path('edit/', views.edit_details_photo, name = 'edit photo')
    ])),
]