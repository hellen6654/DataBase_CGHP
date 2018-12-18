from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'password1', 'password2','last_name', 'first_name','id_TW','phone_number','address','age','gender')
        
        widgets = {
            'email': forms.TextInput(attrs={'class': 'cr-round--lg'}),
            'password1': forms.PasswordInput(attrs={'class': 'cr-round--lg'}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields