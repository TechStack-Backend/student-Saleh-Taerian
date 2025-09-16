from django.contrib import admin
from .models import Project , Developer , Skill
# Register your models here.
admin.site.register(Project)
admin.site.register(Developer)
admin.site.register(Skill)
