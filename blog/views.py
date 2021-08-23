from blog.forms import ShareForm
from django.utils import timezone
from django.utils.translation import templatize
from django.views.generic.base import TemplateView, View
from blog.models import Category, Post
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


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


class BlogListView(ListView):
    template_name = "blog/list.html"
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.filter(
        status=Post.statusChoise.PUBLISHED,
        publish_time__lte=timezone.now())


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


class BlogDetailView(DetailView):
    template_name = "blog/detail.html"
    model = Post
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(
            status=Post.statusChoise.PUBLISHED,
            publish_time__year=self.kwargs["year"],
            publish_time__month=self.kwargs["month"],
            publish_time__day=self.kwargs["day"],
            slug=self.kwargs["slug"])


class SharePost(View):
    def get(self, request, pk):
        form = ShareForm()
        post = get_object_or_404(Post, pk=pk)
        return render(request, "blog/share.html", {'form': form, 'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = ShareForm(request.POST)
        if form.is_valid():
            return redirect(post.get_absolute_url())
        else:
            return render(request, "blog/share.html", {'form': form, 'post': post})
