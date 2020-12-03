from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post_m, Like, Comment, User, Postview
from .forms import PostForm
# Create your views here:

class Post_mListView(ListView):
    model = Post_m

class Post_mDetailView(DetailView):
    model = Post_m
    success_url = '/'

class Post_mCreateView(CreateView):
    model = Post_m
    form_class = PostForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = 'create'
        return context
   
class Post_mDeleteView(DeleteView):
    model = Post_m

class Post_mUpdateView(UpdateView):
    model = Post_m 
    form_class = PostForm
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = 'update'
        return context

def Like_post(request, slug):
    post = get_object_or_404(Post_m, slug=slug)
    like = Like.objects.filter(user=request.user, post=post )
    if like.exists():
        like[0].delete()
        return redirect('detail', slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)