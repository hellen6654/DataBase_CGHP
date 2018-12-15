from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Member

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'password1', 'password2','last_name', 'first_name','id_TW','phone_number','address','age','gender')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class  MemberCreationForm(object):
    """docstring for  MemberCreationForm"""
    def __init__(self, arg):
        super( MemberCreationForm, self).__init__()
        self.arg = arg
        