from django.urls import path
from allauth.account import urls as allauth_urls
# from allauth.account.views import LoginView
from . import views
from django.contrib.auth import views as auth_views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, LikeView, UserEditView, PasswordsChangeView, PostList

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove/', DeletePostView.as_view(), name="delete_post"),
    path('article/<int:pk>/remove/', DeletePostView.as_view(), name="delete_post"),
    path('like/<int:pk>/remove/', LikeView, name="like_post"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    # path('password/', auth_views.PasswordChangeView.as_view(
    # template_name='account/password_change.html'), name='password'),
    path('password/change', PasswordsChangeView.as_view(
        template_name='account/password_change.')),
    path('', PostList.as_view(), name='post_list'),
    # path('article/<int:pk>/comment/', views.post_comment, name='post_comment'),

]
