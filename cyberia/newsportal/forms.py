from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    birthdate = forms.DateField()
    discord_id = forms.CharField(max_length=100, help_text='Discord ID')
    zoom_id = forms.CharField(max_length=100, help_text='Zoom ID')

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "birthdate", "email", "discord_id", "zoom_id"]