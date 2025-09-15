from django.contrib import admin
from .models import Project , Developers , Skill
# Register your models here.
admin.site.register(Project)
admin.site.register(Developers)
admin.site.register(Skill)
