from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect

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