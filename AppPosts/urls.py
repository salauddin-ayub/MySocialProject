from AppPosts import views
from django.urls import path


app_name= 'AppPosts'

urlpatterns = [
    path("", views.home, name='home'),
    path('liked/<pk>/', views.liked, name='liked'),
    path('unliked/<pk>/',views.unliked, name='unliked'),

]
