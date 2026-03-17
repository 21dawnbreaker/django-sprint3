from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post, Category

DISPLAYED_POSTS_AMOUNT = 5


def get_filtered_query_set():
    """Вспомогательная функция, возвращает
    выборку с базовыми фильтрами.
    """
    query_set = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        category__is_published=True,
        is_published=True,
        pub_date__lte=timezone.now(),
    )
    return query_set


def index(request):
    posts_list = get_filtered_query_set()

    context = {
        'posts': posts_list[:DISPLAYED_POSTS_AMOUNT],
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id: int):
    post = get_object_or_404(
        get_filtered_query_set(),
        id=post_id,
    )

    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = get_filtered_query_set().filter(
        category__slug=category_slug,
    )

    context = {
        'post_list': post_list,
        'category': category_slug,
    }
    return render(request, 'blog/category.html', context)
