from django.db import models
from django.contrib.auth.models import User

"""profile table"""
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    names = models.CharField(max_length=100, blank=True)
    location =models.CharField(max_length=50, blank=True)
    url =models.CharField(max_length=50, blank=True)
    bio =models.TextField(blank=True)
    created =models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', 
                                        default='default.jpg')

    def __sttr__(self):
        return f'{self.names} - {self.url}'