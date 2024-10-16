from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

#-> Vista basada en funciones
def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts' : posts})

#-> Vista basada en clases
class PostListView(ListView):
    model = Post
    template_name = "posts/posts.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_individual.html"
    context_object_name = "posts"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()