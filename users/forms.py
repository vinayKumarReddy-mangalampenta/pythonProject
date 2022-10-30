from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile,Skill,Message
# from django.contrib.auth.models import User


class UpdateUserProfile(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user','id']
    def __init__(self, *args, **kwargs):
        super(UpdateUserProfile, self).__init__(*args, **kwargs)

        for k, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text'})

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'name',
            'email': 'email'
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # for k, field in self.fields.items():
        #     field.widget.attrs.update(
        #         {'class': 'input input--text', 'placeHolder': "Enter "+k })
        self.fields['first_name'].widget.attrs.update(
            {'class': 'input input--text', 'placeHolder': "e.g vinay"})
        self.fields['email'].widget.attrs.update(
            {'class': 'input input--text', 'placeHolder': "enter your email"})
        self.fields['username'].widget.attrs.update(
            {'class': 'input input--text', 'placeHolder': "username"})
        self.fields['password1'].widget.attrs.update(
            {'class': 'input input--text', 'placeHolder': "enter password "})
        self.fields['password2'].widget.attrs.update(
            {'class': 'input input--text', 'placeHolder': "confirm password "})

class SkillForm(ModelForm):
    class Meta :
        model = Skill 
        fields = "__all__"
        exclude= ['id','owner']
    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for k, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text'})


class MessagesForm(ModelForm):
    class Meta :
        model = Message 
        fields = "__all__"
        exclude= ['id','sender','receiver','is_read']
    def __init__(self, *args, **kwargs):
        super(MessagesForm, self).__init__(*args, **kwargs)

        for k, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input input--text'})