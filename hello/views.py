from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  if 'msg' in request.GET:
    msg = request.GET['msg']
    print(request.GET)
    result = ('you typed: "' + msg + '".')
  else:
    result = 'please msg parameter'
  return HttpResponse(result)
