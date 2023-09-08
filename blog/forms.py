from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 
    'title_tag',
    'slug',
    'author', 
    'content',
    'featured_image', 
    'excerpt',
    'status', 
    'likes')

widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control'}),
    'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
    'slug': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})),
    'author': forms.Select(attrs={'class': 'form-control'}),
    'content': forms.Textarea(attrs={'class': 'form-control'}),
    'featured_image': forms.ImageField(),
    'excerpt': forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'})),
    'status': forms.ChoiceField(choices=[('draft', 'Draft'), ('published', 'Published')], widget=forms.Select(attrs={'class': 'form-control'})),
    'likes': forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'})),
}