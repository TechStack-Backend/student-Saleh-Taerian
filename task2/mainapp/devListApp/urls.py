from django.contrib import admin
from django.urls import path
from .views import show_users ,show_cv
urlpatterns = [
    path('' ,show_users),
    path('<str:username>/' , show_cv , name= 'show_cv')
]
# مشکل url