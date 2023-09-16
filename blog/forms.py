from django import forms
from .models import Post
from django.urls import reverse_lazy
from allauth.account.forms import SignupForm
from .views import UserChangeForm
from django.contrib.auth.models import User
from django.views import generic


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',
                  'title_tag',
                  'author',
                  'content')


widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control'}),
    'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
    'author': forms.Select(attrs={'class': 'form-control'}),
    'content': forms.Textarea(attrs={'class': 'form-control'}),

}


# forms.py
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',
                  'last_login', 'is_superuser', 'is_active', 'date_joined']

        email = forms.EmailField(widget=forms.EmailInput(
            attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    first_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.DateTimeField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.DateTimeField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))


#######
class CustomSignupForm(SignupForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    first_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
