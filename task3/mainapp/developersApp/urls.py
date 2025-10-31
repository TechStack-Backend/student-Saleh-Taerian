from django.contrib import admin
from django.urls import path
from .views import projectCreateView , developerCreateView , developerListView , projectListview , skillCreateView , developerDetail
urlpatterns = [
    path('login/dev' , developerCreateView.as_view() , name = "addDev"),
    path('login/skill' ,skillCreateView.as_view() , name="addSkill") , 
    path('login/project' , projectCreateView.as_view() , name="addProj"),
    path('developers' , developerListView.as_view() , name="ShowDevs"),
    path('projects' , projectListview.as_view() , name="showProjs"),
    path('eachDev/<int:pk>' , developerDetail.as_view() , name ="showEachDev")
]
