from django.contrib import admin

# Register your models here.
# from instagram.project.models import Project
from project import models


admin.site.register(models.Project)
admin.site.register(models.Review)
admin.site.register(models.Tag)
