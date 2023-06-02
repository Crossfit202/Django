from django.urls import reverse_lazy
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'listing/home.html', context)


def about(request):
    return render(request, 'listing/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'listing/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})