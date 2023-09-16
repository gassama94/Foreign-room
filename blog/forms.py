from django import forms
from .models import Post 
from django.urls import reverse_lazy
from allauth.account.forms import SignupForm 
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
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30, label='First Name', required=True)
    last_name = forms.CharField(
        max_length=30, label='Last Name', required=True)
    

