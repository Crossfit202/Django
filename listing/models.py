from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book_author = models.CharField(max_length=100, default='unknown')
    edition = models.CharField(max_length=100, default='unknown')
    isbn = models.CharField(max_length=100, default='unknown')
    condition = models.CharField(max_length=100, default='unknown')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    contact = models.CharField(max_length=100, default='unknown')
    location = models.CharField(max_length=100, default='unknown')

def __str__(self):
    return self.title


def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk', self.pk})

