from django.urls import path
from . import views

urlpatterns = [
  path('/articles', views.index, name='index'),
  path('/article/<int:num>', views.show, name='show'),
  path('/articles/create', views.create, name='create'),
  path('/article/<int:num>/delete', views.delete, name='delete'),
  path('/article/<int:num>/edit', views.edit, name='edit'),
  path('/books/create', views.book_create, name='book_create'),
]
