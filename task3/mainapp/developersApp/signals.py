from django.dispatch import receiver
from django.db.models.signals import post_migrate, post_save, pre_save
from .models import User, profile, Project
from django.contrib.auth.models import Group, Permission


@receiver(post_migrate)
def createPermissionGroup(sender, **kwargs):
    adminGroup, _ = Group.objects.get_or_create(name="Admin")
    developerGroup, _ = Group.objects.get_or_create(name="Developer")
    managerGroup, _ = Group.objects.get_or_create(name="Managers")
    adminProjPerms = Permission.objects.filter(
        content_type__app_label="developersApp",
        content_type__model="project",
        codename__in=[
            "add_project",
            "change_project",
            "delete_project",
            "view_project",
            "do_project",
        ],
    )
    adminProfPerms = Permission.objects.filter(
        content_type__app_label="developersApp",
        content_type__model="profile",
        codename__in=["change_profile"],
    )
    adminGroup.permissions.set(adminProfPerms | adminProjPerms)
    developerProjPerms = Permission.objects.filter(
        content_type__app_label="developersApp",
        content_type__model="project",
        codename__in=["view_project"],
    )
    developerProfPerms = Permission.objects.filter(
        content_type__app_label="developersApp",
        content_type__model="profile",
        codename__in=["view_profile"],
    )
    developerGroup.permissions.set(developerProfPerms | developerProjPerms)
    managerProjPerms = Permission.objects.filter(
        content_type__app_label="developersApp",
        content_type__model="project",
        codename__in=["add_project", "change_project", "view_project", "do_project"],
    )
    managerProfPerms = Permission.objects.filter(
        content_type__app_label="developersApp",
        content_type__model="profile",
        codename__in=["view_profile"],
    )
    managerGroup.permissions.set(managerProjPerms | managerProfPerms)


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    if instance._state.adding:
        profile.objects.create(user=instance)
        devGroup = Group.objects.get(name="Developer")
        instance.groups.add(devGroup)


@receiver(pre_save, sender=Project)
def add_prefix2(sender, instance, **kwargs):
    if instance._state.adding:
        instance.title = "proj:" + instance.title
