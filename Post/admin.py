from django.contrib import admin
from .models import Post_m, Postview, Like, Comment, User
# Register your models here.

admin.site.register(Post_m)
admin.site.register(Postview)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(User)
