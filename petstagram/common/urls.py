from django.urls import path, include

from petstagram.common import views

urlpatterns = [
    path('', views.home_page_view, name = 'home page')
]