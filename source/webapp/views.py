from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ReviewForm
from webapp.models import Article

def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        data = Article.objects.all()
    else:
        data = Article.objects.filter(status='active')
    return render(request, 'index.html', context={
        'articles': data
    })




def review_create(request):
    if request.method == 'GET':
        form = ReviewForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                author=form.cleaned_data['author'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text']
            )
            return redirect('index')
        else:
            return render(request, 'create.html', context={'form': form})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])



def review_update_view(request, pk):

    article = get_object_or_404(Article, pk=pk)

    if request.method == 'GET':
        form = ReviewForm(initial={
            'author': article.author,
            'email': article.email,
            'text': article.text
        })
        return render(request, 'update.html', context={
            'form': form,
            'article': article
        })

    elif request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            article.author = form.cleaned_data['author'],
            article.email = form.cleaned_data['email'],
            article.text = form.cleaned_data['text'],
            article.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={
                'article': article,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])