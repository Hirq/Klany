from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Rental

# class BookRentView(CreateView):
#     model = Rental
#     fields = ['whoo']
#     template_name = 'Rental/Rental-add.html'
#     success_url = '/'
