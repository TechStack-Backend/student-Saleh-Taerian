from django.shortcuts import render
from .forms import developer_login, add_project, add_skill
from .models import Developer, Skill, Project

# from django.contrib import messages


def add_developer(request):
    if request.method == "POST":
        form = developer_login(request.POST)
        if form.is_valid():
            Developer.objects.create(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                age=form.cleaned_data["age"],
            )
        else:
            print("de akhe!")
    else:
        form = developer_login()
    return render(request, "developersApp/add_dev.html", {"form": form})


def add_proj(request):
    if request.method == "POST":
        form = add_project(request.POST)
        if form.is_valid():
            project = Project.objects.create(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
            )
            project.developers.set(form.cleaned_data["developers"])
            project.save()
        else:
            print("de akhe!")
    else:
        form = add_project()
    return render(request, "developersApp/add_proj.html", {"form": form})


def add_skl(request):
    if request.method == "POST":
        form = add_skill(request.POST)
        if form.is_valid():
            Skill.objects.create(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                developer=form.cleaned_data["developer"],
            )
        else:
            print("de akhe!")
    else:
        form = add_skill()
    return render(request, "developersApp/add_skill.html", {"form": form})


def show_developers(request):
    skills = Skill.objects.all()
    return render(request , 'developersApp/show_developers.html',{'skills':skills})


def show_projects(request):
    projects = Project.objects.all()
    return render(request , 'developersApp/show_projects.html' , {'projects':projects})
