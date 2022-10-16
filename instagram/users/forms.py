from django.forms import ModelForm

from users.models import Profile


class CreateUserProfile(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
