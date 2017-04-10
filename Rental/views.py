from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse

from django.urls import reverse_lazy

from .models import Rental

class BookRentView(CreateView):
    model = Rental
    fields = ['name','whoo','who']
    template_name = 'Rental/Rental-add.html'



# class RentalUpdateView(UpdateView):
#     model = Rental
#     fields = ['name','whoo']
#     template_name_suffix = '_update_form'



class RentDeleteView(DeleteView):
    model = Rental
    template_name = 'Rental/rental_delete.html'
    success_url = '/Rental/List'
    # fields = ['name','whoo']
    # success_url = '/'




class RentListView(ListView):
    model = Rental


class RentDetailView(DetailView):
    model = Rental

class RentListView1(ListView):
    model = Rental
    template_name = 'Rental/rental_list_1.html'

class RentListView6(ListView):
    model = Rental
    template_name = 'Rental/rental_list_6.html'


