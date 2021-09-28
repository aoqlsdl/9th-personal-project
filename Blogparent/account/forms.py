from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields=['username','password1','password2','nickname','university','location']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username','nickname','university','location']