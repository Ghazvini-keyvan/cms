from django.utils import timezone
from blog.models import Category, Post
from django.shortcuts import get_object_or_404, render


def category_view(request):
    categories = Category.objects.all()
    return render(
        request,
        "blog/categories.html",
        {'categories': categories})


def list_view(request):
    posts = Post.objects.filter(
        status=Post.statusChoise.PUBLISHED,
        publish_time__lte=timezone.now())

    # posts = get_object_or_404(
    #     status=Post.statusChoise.PUBLISHED,
    #     publish_time__lte=timezone.now())

    return render(request, "blog/list.html", {'posts': posts})


def detail_view(request, year, month, day, slug):
    post = Post.objects.filter(
        status=Post.statusChoise.PUBLISHED,
        publish_time__year=year,
        publish_time__month=month,
        publish_time__day=day,
        slug=slug).first()

    # post = get_object_or_404(
    #     status=Post.statusChoise.PUBLISHED,
    #     publish_time__year=year,
    #     publish_time__month=month,
    #     publish_time__day=day,
    #     slug=slug)

    return render(request, "blog/detail.html", {'post': post})
