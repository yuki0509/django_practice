from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from . forms import FriendForm
from . models import Friend
from django.views.generic import ListView
from django.views.generic import DetailView
from . forms import FindForm
from django.db.models import Q

# Create your views here.
class FriendList(ListView):
  model = Friend

class FriendDetail(DetailView):
  model = Friend


def index(request):
  data = Friend.objects.all().order_by('age').reverse
  params = {
    'title': 'Hello',
    'data':data,
  }
  return render(request, 'hello/index.html', params)

def create(request):
  if(request.method == 'POST'):
    obj = Friend()
    friend = FriendForm(request.POST, instance=obj)
    friend.save()
    return redirect(to='/hello')
  params = {
    'title': 'Hello',
    'form': FriendForm(),
  }
  return render(request, 'hello/create.html', params)

def edit(request, num):
  obj = Friend.objects.get(id=num)
  if(request.method== 'POST'):
    friend = FriendForm(request.POST, instance=obj)
    friend.save()
    return redirect(to='/hello')
  params = {
    'title': 'Hello',
    'id': num,
    'form': FriendForm(instance=obj),
  }

  return render(request, 'hello/edit.html', params)

def delete(request, num):
  friend = Friend.objects.get(id=num)
  if (request.method == 'POST'):
    friend.delete()
    return redirect(to='/hello')
  params = {
    'title': 'hello',
    'id': num,
    'obj': friend,
  }
  return render(request, 'hello/delete.html', params)

def form(request):
  msg = request.POST['msg']
  params = {
    'title':'Hello',
    'msg':'こんにちは、' + msg + 'さん',
    'goto':'next',
    'number':89898989,
  }
  return render(request, 'hello/index.html', params)

def find(request):
  if(request.method=='POST'):
    msg = 'search result:'
    form = FindForm(request.POST)
    find = request.POST['find']
    list = find.split()
    data = Friend.objects.all()[int(list[0]):int(list[1])]
  else:
    msg = 'search words...'
    form = FindForm()
    data = Friend.objects.all()
  params = {
    'title': 'Hello',
    'message': msg,
    'form': form,
    'data': data,
  }
  return render(request, 'hello/find.html', params)
