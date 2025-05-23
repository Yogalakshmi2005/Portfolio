from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import About, SkillGroup, Skill, Project, Certification, Contact

admin.site.register(About)
admin.site.register(SkillGroup)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(Contact)
