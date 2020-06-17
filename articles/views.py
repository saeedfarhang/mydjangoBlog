from django.shortcuts import render,HttpResponse
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    args = {'articles':articles}
    return render(request, 'articles/articleslist.html', args)

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = models.Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html',{'article':article})

@login_required(login_url = "/accounts/login")
def create_article(request):
    return render(request , 'articles/create_article.html')
