from django.forms import ModelForm

from project.models import Project, Review
from django import forms


class CreateProject(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'thumbnail', 'description',
                  'demo_link', 'source_code', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(CreateProject, self).__init__(*args, **kwargs)

        for k, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text', 'placeHolder': "add " + k})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': "place your vote",
            'body': "review"
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for k, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text'})

        # self.fields['body'].widget.attrs.update({'class': 'input', 'placeHolder': "Enter your review"})
        self.fields['value'].widget.attrs.update({'class': 'input custom-select', 'value': "Select"})
