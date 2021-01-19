from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from . forms import HelloForm

# Create your views here.

class HelloView(TemplateView):

  def __init__(self):
    self.params = {
      'title':'Hello',
      'form': HelloForm(),
      'result':None,
    }

  def get(self,request):
    return render(request, 'hello/index.html', self.params)

  def post(self, request):
    ch = request.POST['choice']
    self.params['result'] = 'you selected: "' + ch + '".'
    self.params['form'] = HelloForm(request.POST)
    return render(request, 'hello/index.html', self.params)


def next(request):
  params = {
    'title':'hello/next',
    'msg':'これはページでスヨン。',
    'goto':'index',
    'number':89898989,
  }
  return render(request, 'hello/index.html', params)

def form(request):
  msg = request.POST['msg']
  params = {
    'title':'Hello',
    'msg':'こんにちは、' + msg + 'さん',
    'goto':'next',
    'number':89898989,
  }
  return render(request, 'hello/index.html', params)
