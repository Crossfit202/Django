from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
    # Define a one-to-one relationship with the User model. This means that when the profile is deleted, the posts they have made are deleted, but the profile is not deleted when the posts are deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Define an image field with a default image and upload directory
    image = models.ImageField(default='default.jpg', upload_to='profile.pics')

    def __str__(self):
        # Return a string representation of the profile, including the username
        return f'{self.user.username} Profile'
    

