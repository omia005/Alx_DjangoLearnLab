from django.urls import path 
from . import views
from .views import PostCreateView,PostListView,PostDetailView,PostDeleteView,PostUpdateView,CommentCreateView, CommentUpdateView, CommentDeleteView,PostByTagListView

urlpatterns = [
  
    path('login/', views.login_view,  name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('', views.home_view, name='home'),
    path('post/new/', PostCreateView.as_view(), name='new-post'),
    path('post-list/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name="add-comment"),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update-comment'),
    path('comment/<int:pk>/delete/',CommentDeleteView.as_view(), name='delete-comment'),
    path('tags/<slug:tag_slug>/', PostListView.as_view(), name='posts-by-tag'),
    path('search/', PostByTagListView.as_view(), name='search-posts'),
    path("tags/<slug:tag_slug>/", views.posts_by_tag, name="posts-by-tag"),
  
]

   