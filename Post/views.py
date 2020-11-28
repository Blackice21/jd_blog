from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post_m, Like, Comment, User, Postview
# Create your views here:

class Post_mListView(ListView):
    model = Post_m

class Post_mDetailView(DetailView):
    model = Post_m
    success_url = '/'

class Post_mCreateView(CreateView):
    model = Post_m
    fields = [
        'title',  
        'content',  
        'thumbnail',    
        'author', 
        'slug', 
    ]

class Post_mDeleteView(DeleteView):
    model = Post_m

class Post_mUpdateView(UpdateView):
    model = Post_m 
    fields = [
        'title',  
        'content',  
        'thumbnail',    
        'author', 
        'slug', 
    ]