from typing import Any
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from allauth.account.views import PasswordChangeView
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from .views import UserEditView
from .models import Post, Comment
from .forms import PostForm, EditProfileForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'account/password_change.html'
    # success_url = reverse_lazy('home')
    success_url = '/accounts/login/'
    


    def form_valid(self, form):
        # Call the parent class's form_valid method to perform the password change
        response = super().form_valid(form)

        # Redirect to the Allauth login page
        return redirect(self.get_success_url())

    # def get_object(self):
    #     return self.request.user


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-created_on']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        # post = self.object

        liked = False
        if self.request.user.is_authenticated and post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comments = Comment.objects.filter(post=post)

        context['liked'] = liked  # Add the 'liked' variable to the context
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        return context



    def post(self, request, **kwargs):
        # context = super().get_context_data(**kwargs)
        # queryset = Post.objects.filter(status=1)
         post = get_object_or_404(Post, id=self.kwargs['pk'])
         comments = post.comments.filter(approved=True).order_by("-created_on")
         comment_form = CommentForm(data=request.POST)

         liked = False
         if post.likes.filter(id=self.request.user.id).exists():
              liked = True

         comments = Comment.objects.filter(post=post)
         comment_form = CommentForm(data=request.POST)

         if comment_form.is_valid():
             comment_form.instance.email = request.user.email
             comment_form.instance.name = request.user.username
             comment = comment_form.save(commit=False)
             comment.post = post
             comment.save()
             return redirect('article-detail', pk=post.pk)
         else:
             comment_form = CommentForm()

         return render(
             request,
             "article_details.html",
             {
                 "post": post,
                 "comments": comments,
                 "commented": True,
                 "comment_form": comment_form,
               
             },
         )


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = ('title',
    # 'title_tag',
    # 'author',
    # 'content',
    # 'featured_image',
    # 'status')
    # fields = '__all__'
    # fields = ('title', 'content')


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'title_tag', 'content']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "home.html"
    paginate_by = 6
