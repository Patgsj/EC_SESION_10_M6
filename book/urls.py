from django.urls import path
from . import views

urlpatterns = [
    path('', views.boards_home, name='boards_home'),
]
