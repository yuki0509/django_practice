from django.urls import path
from . import views

urlpatterns = [
  path('/articles', views.index, name='index'),
  path('/article/<int:num>', views.show, name='show'),
]
