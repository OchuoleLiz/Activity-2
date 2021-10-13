from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render
from django.template import RequestContext


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post.html'

def entry_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)
