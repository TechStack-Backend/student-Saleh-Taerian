from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import developer_login, add_project, add_skill, userSignup
from .models import Developer, Skill, Project, profile
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from .forms import add_project, add_skill, developer_login, profileForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from functools import wraps
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
# from django.contrib import messages


class developerCreateView(LoginRequiredMixin, CreateView):
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


class projectCreateView(LoginRequiredMixin, CreateView):
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


class skillCreateView(LoginRequiredMixin, CreateView):
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


class developerListView(LoginRequiredMixin, ListView):
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


class projectListview(LoginRequiredMixin,PermissionRequiredMixin , ListView):
    model = Project
    template_name = "developersApp/show_projects.html"
    context_object_name = "projects"
    permission_required = "developersApp.do_Project"

    def get_queryset(self):
        return super().get_queryset()


# def show_projects(request):
#     projects = Project.objects.all()
#     return render(request , 'developersApp/show_projects.html' , {'projects':projects})
class developerDetail(LoginRequiredMixin, DetailView):
    model = Developer
    template_name = "developersApp/single_developer.html"
    context_object_name = "developer"


class deleteDeveloper(LoginRequiredMixin, DeleteView):
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


class deleteSkill(LoginRequiredMixin, DeleteView):
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


class deleteProject(LoginRequiredMixin, DeleteView):
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


class updateDeveloper(LoginRequiredMixin, UpdateView):
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


class updateProject(LoginRequiredMixin, UpdateView):
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


class updateSkill(LoginRequiredMixin, UpdateView):
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


class aboveLegalAge(LoginRequiredMixin, ListView):
    model = Developer
    template_name = "developersApp/legalAge.html"
    context_object_name = "developers"

    def get_queryset(self):
        return super().get_queryset().filter(age__gte=18)


# class registerUser(CreateView):
#     form_class = userSignup
#     template_name = "developersApp/userSignup.html"
#     success_url = reverse_lazy("userLogin")


# class userLogin(View):
#     template_name = "developersApp/userLogin.html"
#     def get(self ,request):
#         form = userSignin()
#         return render(request , self.template_name ,{'form':form})
#     def post(self , request):
#         form = userSignin(request.POST)
#         if form.is_valid():
#             userName = form.cleaned_data['userName']
#             password = form.cleaned_data['password']
#             user = authenticate(request ,username=userName ,password= password)
#             if user:
#                 login(request ,user)
#                 return redirect("showEachDev")
#         return render(request , self.template_name ,{'form':form})


class userSignup(CreateView):
    model = User
    form_class = userSignup
    template_name = "developersApp/userSignup.html"

    def get_success_url(self):
        return reverse_lazy("userLogin")


class userSignin(LoginView):
    template_name = "developersApp/userLogin.html"
    redirect_authenticated_user = True


class userLogout(LogoutView):
    next_page = reverse_lazy("userLogin")


class updateProfile(LoginRequiredMixin, UpdateView):
    template_name = "developersApp/updateProfile.html"
    model = profile
    form_class = profileForm
    success_url = reverse_lazy("updateProfile")

    def get_object(self):
        prof, created = profile.objects.get_or_create(user=self.request.user)
        return prof


class myProfile(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    raise_exception = True
    template_name = "developersApp/myProfile.html"


@permission_required("developersApp.view_Developer" , raise_exception=True)
def show_devs(request):
    developers = Developer.objects.all()
    return render(request, "show_developers.html", {"devs": developers})

def owner_required(model , id):
    def decorator(func):
        @wraps(func)
        def wrapper(request , *args , **kwargs):
            obj = model.objects.get(pk = kwargs[id])
            if(obj.developer != request.user):
                return HttpResponseForbidden
            return func(request , *args , **kwargs)
        return wrapper
    return decorator

# class OwnerOrPermissionMixin:
#     permission_required  = None
#     def is_authorized(self):
#         obj = self.get_object()
#         user = self.request.user
#         if obj.developer==user or (user.has_perm(self.permission_required) and permission_required):
#             return True
#         return False
#     def dispatch(self , request , *args , **kwargs):
#         if not self.is_authorized:
#             return PermissionDenied
#         return super().dispatch(self , request , *args , **kwargs)