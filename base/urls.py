from django.urls import path
from . import views

urlpatterns = [
   path('', views.Home.as_view(), name='home'),
    path('projects/', views.Projects.as_view(), name='projects'),
]