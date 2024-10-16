from django.urls import path
from .views import posts            #-> Vista basada en funciones
from .views import PostListView, PostDetailView     #-> Vista basada en clases
from . import views

app_name = 'apps.posts'

urlpatterns = [
    #-> Vista basada en funciones
    #path('posts/', posts, name='posts'),

    #-> Vista basada en clases
    path('posts/', PostListView.as_view(), name='posts'),
    path("posts/<int:id>/", PostDetailView.as_view(), name="post_individual"),
    
]