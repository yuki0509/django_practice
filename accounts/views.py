from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from . forms import LoginForm, SignUpForm

# Create your views here.

class Login(LoginView):
  #ログインページ
  form_class = LoginForm
  template_name = 'accounts/login.html'

class Logout(LoginRequiredMixin,LogoutView):
  template_name = 'accounts/login.html'

def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = SignUpForm()
  params = {'form':form}
  return render(request, 'accounts/signup.html', params)
