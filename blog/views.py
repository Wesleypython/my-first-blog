from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
"""E isso é exatamente o que as views devem fazer: conectar modelos e templates"""
"""Em uma view, nós decidimos o que (qual modelo) será exibido em um template."""


def post_list(request): 
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {})


