#coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.views.generic import ListView, DetailView


from django.shortcuts import render

# Create your views here.
from .models import Author

class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author