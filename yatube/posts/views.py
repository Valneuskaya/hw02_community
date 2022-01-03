from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404, render

from .models import Group, Post, User


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/index.html'
    context = {'posts': posts, 'page_obj': page_obj, }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group_posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/group_list.html'
    context = {'group': group, 'posts': posts, 'page_obj': page_obj, }
    return render(request, template, context)


def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    user = get_object_or_404(User, username=username)
    posts = user.group_posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/profile.html'
    title = 'Профайл пользователя ' + username
    context = {
        'title': title,
        'page_obj': page_obj,
        'posts': posts,
        'user': user,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    count = Post.objects.filter(author=post.author).count()
    title = 'Пост ' + post.text[:30]
    template = 'posts/post_detail.html'
    context = {
        'post': post,
        'count': count,
        'title': title,
    }
    return render(request, template, context)
