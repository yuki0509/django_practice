from django.shortcuts import render
from . models import Article

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
