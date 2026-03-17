import datetime

from django.shortcuts import render, get_object_or_404, get_list_or_404
from blog.models import Post, Category, Location
from tests.fixtures.fixture_data import published_category


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
    post = get_object_or_404(
        Post.objects.select_related('category', 'location'),
        id=post_id,
        pub_date__lte=datetime.datetime.now(),
        is_published=True,
        category__is_published=True,
    )

    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    post_list = Post.objects.select_related(
            'category', 'location',
        ).filter(
            category__is_published=category.is_published,
            category__slug=category_slug,
            pub_date__lte=datetime.datetime.now(),
        )

    context = {
        'post_list': post_list,
        'category': category_slug,
    }
    print(context)
    return render(request, 'blog/category.html', context)
