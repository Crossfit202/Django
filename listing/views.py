from typing import Optional
from django.urls import reverse_lazy
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def home(request):
    # Retrieve all Post objects from the database
    context = {
        'posts': Post.objects.all()
    }
    # Render the home template with the Post objects in the context
    return render(request, 'listing/home.html', context)

def about(request):
    # Render the about template
    return render(request, 'listing/about.html')

class PostListView(ListView):
    # Set the model to Post
    model = Post
    # Set the template name
    template_name = 'listing/home.html'
    # Set the name of the context object to 'posts'
    context_object_name = 'posts'
    # Set the ordering of the posts to show the most recent ones first
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    # Set the model to Post
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    # Set the model to Post
    model = Post
    # Set the fields to be included in the form
    fields = ['title', 'content', 'book_author', 'edition', 'course', 'isbn', 'condition', 'price', 'contact', 'location']

    def form_valid(self, form):
        # Set the author of the post to the current user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect the user to the detail view of the newly created post
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # Set the model to Post
    model = Post
    # Set the fields to be included in the form
    fields = ['title', 'content', 'book_author', 'edition', 'course', 'isbn', 'condition', 'price', 'contact', 'location']

    def form_valid(self, form):
        # Set the author of the post to the current user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # Check if the current user is the author of the post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        # Redirect the user to the detail view of the updated post
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # Set the model to Post
    model = Post
    # Set the URL to redirect to after successful deletion
    success_url = '/'

    def test_func(self):
        # Check if the current user is the author of the post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False