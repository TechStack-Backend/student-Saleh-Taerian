from django.contrib import admin
from django.urls import path
from .views import (
    projectCreateView,
    developerCreateView,
    developerListView,
    projectListview,
    skillCreateView,
    developerDetail,
    deleteProject,
    deleteSkill,
    deleteDeveloper,
    updateDeveloper,
    updateProject,
    updateSkill,
    aboveLegalAge,
    registerUser,
    userLogin
)

urlpatterns = [
    path("add/dev", developerCreateView.as_view(), name="addDev"),
    path("add/skill", skillCreateView.as_view(), name="addSkill"),
    path("add/project", projectCreateView.as_view(), name="addProj"),
    path("developers", developerListView.as_view(), name="ShowDevs"),
    path("projects", projectListview.as_view(), name="showProjs"),
    path("eachDev/<int:pk>", developerDetail.as_view(), name="showEachDev"),
    path("delete/developer/<int:pk>", deleteDeveloper.as_view(), name="deleteDev"),
    path("delete/project/<int:pk>", deleteSkill.as_view(), name="deleteSkill"),
    path("delete/skill/<int:pk>", deleteProject.as_view(), name="deleteProject"),
    path("update/developer/<int:pk>", updateDeveloper.as_view(), name="updateDev"),
    path("update/project/<int:pk>", updateProject.as_view(), name="updateProj"),
    path("update/skill/<int:pk>", updateSkill.as_view(), name="updateSkill"),
    path("aboveLegalDevs", aboveLegalAge.as_view(), name="aboveLegal"),
    path("register/", registerUser.as_view(), name="userSignup"),
    path("login/", userLogin(), name="userLogin"),
    
]
