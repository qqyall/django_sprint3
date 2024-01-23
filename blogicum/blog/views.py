from datetime import datetime

from typing import Any

from django.shortcuts import get_object_or_404, render, get_list_or_404

from .models import Post, Category


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.all().filter(
        is_published=True,
        category__is_published=True,
        pub_date__lt=datetime.utcnow()
    ).order_by('-created_at')[:5]

    context = {
        'post_list': post_list
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lt=datetime.utcnow()
        ),
        pk=post_id
    )

    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    post_list = get_list_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lt=datetime.utcnow()
        ),
        category__slug=category_slug
    )

    category = get_object_or_404(
        Category.objects.filter(
            slug=category_slug
        )
    )

    context = {'post_list': post_list, 'category': category}
    return render(request, template, context)
