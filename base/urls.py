from django.urls import path
from . import views

urlpatterns = [
   path('', views.Home.as_view(), name='home'),
   path('projects/', views.Projects.as_view(), name='projects'),
   path('about/', views.About.as_view(), name='about'),
   path('newsletter/', views.Newsletter.as_view(), name='newsletter'),
   path('articles/', views.Articles.as_view(), name='articles'),
]