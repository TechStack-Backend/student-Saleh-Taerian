from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import developer_login, add_project, add_skill
from .models import Developer, Skill, Project
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from .forms import add_project, add_skill, developer_login
from django.contrib import messages

# from django.contrib import messages


class developerCreateView(CreateView):
    model = Developer
    template_name = "developersApp/add_dev.html"
    form_class = developer_login
    success_url = reverse_lazy("addDev")

    def form_valid(self, form):
        messages.success(self.request, "adding  was successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "adding wasn't successful")
        return super().form_invalid(form)


# def add_developer(request):
#     if request.method == "POST":
#         form = developer_login(request.POST)
#         if form.is_valid():
#             Developer.objects.create(
#                 first_name=form.cleaned_data["first_name"],
#                 last_name=form.cleaned_data["last_name"],
#                 email=form.cleaned_data["email"],
#                 age=form.cleaned_data["age"],
#             )
#         else:
#             print("de akhe!")
#     else:
#         form = developer_login()
#     return render(request, "developersApp/add_dev.html", {"form": form})


class projectCreateView(CreateView):
    model = Project
    form_class = add_project
    template_name = "developersApp/add_proj.html"
    form_class = add_project
    success_url = reverse_lazy("addProj")

    def form_valid(self, form):
        messages.success(self.request, "adding  was successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "adding wasn't successful")
        return super().form_invalid(form)

    # model.developers.set(form.cleaned_data["developers"])


# def add_proj(request):
#     if request.method == "POST":
#         form = add_project(request.POST)
#         if form.is_valid():
#             project = Project.objects.create(
#                 title=form.cleaned_data["title"],
#                 description=form.cleaned_data["description"],
#             )
#             project.developers.set(form.cleaned_data["developers"])
#             project.save()
#         else:
#             print("de akhe!")
#     else:
#         form = add_project()
#     return render(request, "developersApp/add_proj.html", {"form": form})


class skillCreateView(CreateView):
    model = Skill
    template_name = "developersApp/add_skill.html"
    form_class = add_skill
    success_url = reverse_lazy("addSkill")

    def form_valid(self, form):
        messages.success(self.request, "adding  was successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "adding wasn't successful")
        return super().form_invalid(form)


# def add_skl(request):
#     if request.method == "POST":
#         form = add_skill(request.POST)
#         if form.is_valid():
#             Skill.objects.create(
#                 title=form.cleaned_data["title"],
#                 description=form.cleaned_data["description"],
#                 developer=form.cleaned_data["developer"],
#             )
#         else:
#             print("de akhe!")
#     else:
#         form = add_skill()
#     return render(request, "developersApp/add_skill.html", {"form": form})


class developerListView(ListView):
    model = Project
    template_name = "developersApp/show_developers.html"
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["developers"] = list(
            Developer.objects.values_list("first_name", flat=True)
        )
        return context


# def show_developers(request):
#     skills = Skill.objects.all()
#     return render(request , 'developersApp/show_developers.html',{'skills':skills})


class projectListview(ListView):
    model = Project
    template_name = "developersApp/show_projects.html"
    context_object_name = "projects"

    def get_queryset(self):
        return super().get_queryset()


# def show_projects(request):
#     projects = Project.objects.all()
#     return render(request , 'developersApp/show_projects.html' , {'projects':projects})
class developerDetail(DetailView):
    model = Developer
    template_name = "developersApp/single_developer.html"
    context_object_name = "developer"


class deleteDeveloper(DeleteView):
    model = Developer
    template_name = "developersApp/deleteDev.html"
    context_object_name = "developer"
    success_url = reverse_lazy("addDev")

    def form_valid(self, form):
        messages.success(self.request, "deleting was successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "deleting wasn't successful")
        return super().form_invalid(form)


class deleteSkill(DeleteView):
    model = Skill
    template_name = "developersApp/deleteSkill.html"
    context_object_name = "skill"
    success_url = reverse_lazy("addSkill")

    def form_valid(self, form):
        messages.success(self.request, "deleting was successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "deleting wasn't successful")
        return super().form_invalid(form)


class deleteProject(DeleteView):
    model = Project
    template_name = "developersApp/deleteProj.html"
    context_object_name = "project"
    success_url = reverse_lazy("addProj")

    def form_valid(self, form):
        messages.success(self.request, "deleting was successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "deleting wasn't successful")
        return super().form_invalid(form)


class updateDeveloper(UpdateView):
    model = Developer
    template_name = "developersApp/update_dev.html"
    context_object_name = "developer"
    form_class = developer_login
    success_url = reverse_lazy("addDev")

    def form_valid(self, form):
        messages.success(self.request, "update was successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "update wasn't successful")
        return super().form_invalid(form)


class updateProject(UpdateView):
    model = Project
    template_name = "developersApp/update_project.html"
    context_object_name = "project"
    form_class = add_project
    success_url = reverse_lazy("addDev")

    def form_valid(self, form):
        messages.success(self.request, "update was successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "update wasn't successful")
        return super().form_invalid(form)


class updateSkill(UpdateView):
    model = Skill
    template_name = "developersApp/update_skill.html"
    context_object_name = "developer"
    form_class = add_skill
    success_url = reverse_lazy("addDev")

    def form_valid(self, form):
        messages.success(self.request, "update was successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "update wasn't successful")
        return super().form_invalid(form)


class aboveLegalAge(ListView):
    model = Developer
    template_name = "developersApp/legalAge.html"
    context_object_name = "developers"

    def get_queryset(self):
        return super().get_queryset().filter(age__gte=18)
