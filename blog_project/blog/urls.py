from django.urls import path
from .views import *

urlpatterns = [
    # JWT AUTH
    path('api/register/', RegisterView.as_view()),

    # Blog CRUD
    path('api/blogs/', BlogListView.as_view()),
    path('api/blogs/create/', BlogCreateView.as_view()),
    path('api/blogs/<int:pk>/', BlogRetrieveView.as_view()),
    path('api/blogs/<int:pk>/update/', BlogUpdateView.as_view()),
    path('api/blogs/<int:pk>/delete/', BlogDestroyView.as_view()),

    # Comment CRUD
    path('api/comments/', CommentListView.as_view()),
    path('api/comments/create/', CommentCreateView.as_view()),
    path('api/comments/<int:pk>/', CommentRetrieveView.as_view()),
    path('api/comments/<int:pk>/update/', CommentUpdateView.as_view()),
    path('api/comments/<int:pk>/delete/', CommentDestroyView.as_view()),

    # HTML Pages
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('create/', create_blog, name='blog_create'),
    path('update/<int:pk>/', blog_update, name='blog_update'),
    path('delete/<int:pk>/', blog_delete, name='blog_delete'),
    path('blog/<int:pk>/', blog_detail, name='blog_detail'),
]
