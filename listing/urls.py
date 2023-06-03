from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views


urlpatterns = [
    # URL pattern for the home page, mapped to the PostListView
    path('', PostListView.as_view(), name='listing-home'),

    # URL pattern for a specific post's detail page, mapped to the PostDetailView
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # URL pattern for updating a specific post, mapped to the PostUpdateView
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    # URL pattern for deleting a specific post, mapped to the PostDeleteView
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # URL pattern for creating a new post, mapped to the PostCreateView
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    # URL pattern for the about page, mapped to the views.about function
    path('about/', views.about, name='listing-about'),
]

