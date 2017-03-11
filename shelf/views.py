#coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import Author, Book

class MainPageView(TemplateView):
    template_name = 'index.html'

index_view = MainPageView.as_view()

# def index_view(request, *args, **kwargs):
#     return HttpResponse('OK - funkcja')




class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):

    model = Author

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

