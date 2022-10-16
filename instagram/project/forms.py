from django.forms import ModelForm

from project.models import Project


class CreateProject(ModelForm):
    class Meta:
        model = Project
        fields = ['title','thumbnail','description','demo_link','source_code','tags']
