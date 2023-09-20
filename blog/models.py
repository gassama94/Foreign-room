from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_img = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    title_tag = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    author = models. ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    content = RichTextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    # featured_image = CloudinaryField('image', default='placeholder')
    header_image = models.ImageField(
        null=True, blank=True, upload_to='images/')
    # excerpt = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models. IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    name = models.CharField(max_length=500)
    post = models. ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.post.title} by {self.name}"
