from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

# Create your models here.
class User(AbstractUser):
    pass
    def __str__(self):
        return self.username

class Post_m(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={'slug':self.slug})

class Comment(models.Model):
    post = models.ForeignKey(Post_m, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Postview(models.Model):
     post = models.ForeignKey(Post_m, on_delete=models.CASCADE)
     timestamp = models.DateTimeField(auto_now_add=True)
     user =  models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
        return self.user.username

class Like(models.Model):
    post = models.ForeignKey(Post_m, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

