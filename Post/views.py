from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post_m, Like, Comment, User, Postview
from .forms import PostForm, CommentForm
# Create your views here:

class Post_mListView(ListView):
    model = Post_m

class Post_mDetailView(DetailView):
    model = Post_m
    success_url = '/'

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.author = self.request.user
            comment.post = post
            comment.save()
            return redirect('detail', slug=post.slug)
        return redirect('detail', slug=self.get_object().slug)    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            Postview.objects.get_or_create(user = self.request.user, post=object)
        return object
        
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
    success_url = '/'

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

def search(request):
    post = Post_m.objects
    keywords = request.GET['keywords']
    if keywords:
        search_post = post.filter(title__icontains=keywords)
        return render(request, 'Post/search.html', {'search_post': search_post, 'keywords': keywords})
    else:
        return redirect('list')