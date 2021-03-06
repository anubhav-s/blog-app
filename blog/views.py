from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BlogDb
from .forms import PostForm


def blog_list(request):
    """
    This method lists all the blogs reading from the database and post it to the html page.
    :param request:
    :return:
    """
    # posts = BlogDb.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    object_list = BlogDb.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/blog_list.html', {'page': page, 'posts': posts})


def blog_detail(request, pk):
    """
    This view method is used to see a particular blog in detail on a html page.
    :param request:
    :param pk:
    :return:
    """
    post = get_object_or_404(BlogDb, pk=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})


def blog_new(request):
    """
    This method is called when new blog has to be created and saves the content in database.
    The content from the text fields of the form is read and stored in database.
    :param request:
    :return:
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/blog_edit.html', {'form': form})


def blog_edit(request, pk):
    """
    This method is called when editing the existing blog and saves the content in database.
    The content to be edited from the text fields is read from the form and saved in database.
    :param request: This is the default parameter for creating a view
    :return:
    """
    post = get_object_or_404(BlogDb, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/blog_edit.html', {'form': form})
