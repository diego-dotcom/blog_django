from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def lista_post(request):
    posts = Post.objects.filter(fecha_publicado__lte=timezone.now()).order_by('fecha_publicado')
    return render(request, 'blog/lista_post.html', {
        'posts': posts
    })