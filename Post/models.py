from django.db import models

# Create your models here.
class Post_m(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post_m, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    # author = models.ForeignKey()

     def __str__(self):
        return self.user.username

class Postview(models.Model):
     post = models.ForeignKey(Post_m, on_delete=models.CASCADE)
     timestamp = models.DateTimeField(auto_now_add=True)
     # user =  models.ForeignKey()

     def __str__(self):
        return self.user.username

class like(models.Model):
    post = models.ForeignKey(Post_m, on_delete=models.CASCADE)
    # user = models.ForeignKey()

    def __str__(self):
        return self.user.username

