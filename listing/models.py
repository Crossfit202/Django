from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    # Fields in the Post model.
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book_author = models.CharField(max_length=100, default='unknown author')
    edition = models.CharField(max_length=100, default='unknown edition')
    course = models.CharField(max_length=100, default='unknown course')
    isbn = models.CharField(max_length=100, default='unknown isbn')
    condition = models.CharField(max_length=100, default='unknown condition')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    contact = models.CharField(max_length=100, default='unknown contact info')
    location = models.CharField(max_length=100, default='unknown location')

def __str__(self):
    return self.title


def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk', self.pk})

