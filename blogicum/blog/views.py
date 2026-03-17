import datetime

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category, Location


def index(request):
    context = {
        'posts': Post.objects.select_related(
            'category', 'location',
        ).filter(
            pub_date__lte=datetime.datetime.now(),
            is_published=True,
            category__is_published=True,
        ).order_by('-pub_date')[:5],
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
    published_category = get_object_or_404(Category, slug=category_slug).is_published
    context = {
        'category_slug': Post.objects.select_related(
            'category', 'location',
        ).filter(
            category__is_published=published_category,
            category__slug=category_slug,
            pub_date__lte=datetime.datetime.now(),
        ),
    }
    return render(request, 'blog/category.html', context)
