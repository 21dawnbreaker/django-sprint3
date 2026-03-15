from django.http import Http404
from django.shortcuts import render



post_per_key = dict()
for post in posts:
    post_per_key[post['id']] = post


def index(request):
    context = {
        'posts': reversed(posts),
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id: int):
    if post_id not in post_per_key:
        raise Http404('Post not found')
    context = {
        'post': post_per_key[post_id],
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    context = {
        'category_slug': category_slug,
    }
    return render(request, 'blog/category.html', context)
