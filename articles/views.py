from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


# Create your views here.

@login_required
def index(request):
    articles = Article.objects.all().order_by('title')

    data = {
        "articles": articles,
    }

    return render(request, 'articlesIndex.html', data)


@login_required
def show(request, id):
    article = get_object_or_404(Article, id=id)

    comments = article.comments_set.all()

    data = {
        "article": article,
        "comments": comments,
    }

    return render(request, 'articlesShow.html', data)


@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'articlesCreate.html')


@login_required
def edit(request, id):
    article = get_object_or_404(Article, id=id)

    if request.user.id != article.created_by:
        raise PermissionDenied

    if request.method == "POST":
        form = ArticleForm(request.POST or None, instance=article)

        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'articlesEdit.html', {"article": article})


@login_required
def delete(request, id):
    article = get_object_or_404(Article, id=id)

    if request.user.id != article.created_by:
        raise PermissionDenied

    article.delete()

    return redirect('index')
