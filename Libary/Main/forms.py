from django.contrib.auth.models import User
from .models import Books
from django.forms import ModelForm


class RegistrateForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')





class BookAddForm(ModelForm):
    class Meta:
        model = Books
        fields = ('name', 'author')