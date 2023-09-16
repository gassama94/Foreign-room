from django.urls import path
#from allauth.account.views import LoginView
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, LikeView, UserEditView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove/', DeletePostView.as_view(), name="delete_post"),
    path('article/<int:pk>/remove/', DeletePostView.as_view(), name="delete_post"),
    path('like/<int:pk>/remove/', LikeView, name="like_post"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
]


