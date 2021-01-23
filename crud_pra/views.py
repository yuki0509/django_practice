from django.shortcuts import render, redirect
from . models import Article
from . forms import ArticleForm

# Create your views here.
def index(request):
  data = Article.objects.all()
  params = {
    'data':data
  }
  return render(request, 'crud_pra/index.html', params)

def show(request, num):
  data = Article.objects.get(id=num)
  params = {
    'data':data
  }
  return render(request, 'crud_pra/show.html', params)

#入力画面出力とレコード作成を両方含む
def create(request):
  if(request.method == 'POST'):
    obj = Article()
    article = ArticleForm(request.POST, instance=obj)
    article.save()
    return redirect(to='index')
  params = {
    'form': ArticleForm()
  }
  return render(request, 'crud_pra/create.html', params)

def delete(request, num):
  article = Article.objects.get(id=num)
  article.delete()
  return redirect(to='index')

def edit(request, num):
  obj = Article.objects.get(id=num)
  if (request.method == 'POST'):
    article = ArticleForm(request.POST, instance=obj)
    article.save()
    return redirect(to='index')
  params = {
    'form':ArticleForm(instance=obj),
    'id':num,
  }
  return render(request, 'crud_pra/edit.html', params)
