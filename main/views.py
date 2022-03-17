from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseRedirect
from .models import Article
from .forms import ArticleForm

def index(request):
  articles = Article.objects.order_by('-id')
  return render(request, 'main/index.html', {'title': 'Main page', 'articles': articles})

def about(request):
  return render(request, 'main/about.html', {'title': 'About us'})

def create(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  article = ArticleForm()
  context = {
    'title': 'Create article',
    'article': article,
  }
  return render(request,'main/create.html', context)

def detail(request, article_id):
  try:
      a = Article.objects.get(id = article_id)
  except:
        raise Http404('Статья не найена')
  return render(request, 'main/detail.html', {'article': a})