from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def lista_post(request):
    posts = Post.objects.filter(fecha_publicado__lte=timezone.now()).order_by('-fecha_publicado')
    return render(request, 'blog/lista_post.html', {
        'posts': posts
    })

def post_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detalle.html', {'post': post})

def post_nuevo(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            #post.fecha_publicado = timezone.now()
            post.save()
            return redirect('post_detalle', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'blog/post_editar.html', {'form': form})


def post_editar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.fecha_publicado = timezone.now()
            post.save()
            return redirect('post_detalle', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_editar.html', {'form': form})


def post_lista_borradores(request):
    posts = Post.objects.filter(fecha_publicado__isnull=True).order_by('fecha_creado')
    return render(request, 'blog/post_lista_borradores.html', {
        'posts': posts
    })


def post_publicar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publicar()
    return redirect('post_detalle', pk=pk)


def post_eliminar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('lista_post')