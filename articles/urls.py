from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<id>/show/', views.show, name="show"),
    path('create/', views.create, name="create"),
    path('<id>/edit/', views.edit, name="edit"),
    path('<id>/delete/', views.delete, name="delete"),
]