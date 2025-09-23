from django.contrib import admin
from django.urls import path
from .views import add_developer , add_proj , add_skl ,show_developers ,show_projects

urlpatterns = [
    path('login/dev' , add_developer),
    path('login/skill' ,add_skl) , 
    path('login/project' , add_proj),
    path('developers' , show_developers),
    path('projects' , show_projects)
]
