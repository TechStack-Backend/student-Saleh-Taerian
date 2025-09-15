from django.contrib import admin
from django.urls import path
from .views import show_sudents
urlpatterns = [
    path("developers/" , show_sudents)
]
