from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
# def home(request):
# return render(request, 'home.html', {})


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

         liked = False
         if self.request.user.is_authenticated and post.likes.filter(id=self.request.user.id).exists():
             liked = True

             context['liked'] = liked  # Add the 'liked' variable to the context
         return context
         



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
   
   
