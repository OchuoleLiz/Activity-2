from django.http.response import Http404, HttpResponseNotFound, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import get_object_or_404, render


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post.html'

def blogDetailView(request, pk):
    post = get_object_or_404(Post, pk)
    return render(request, 'blog/post.html', context={'post': post})