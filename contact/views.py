from django.shortcuts import render
from django.views.generic import DetailView, FormView
from .models import Message
from .forms import MessageForm, ContactForm

#class MessageDetailView(DetailView):
#    model = Message

class MessageAddView(FormView):
    form_class = ContactForm
    template_name = 'contact/message_detail.html'
    success_url = '/'

 #   def form_valid(self, form):
 #       form.save()
 #       return super (MessageAddView, self).form_valid(self)
    ## GDY FORMULARZ JEST POPRAWNY TO WYKONUJE ISE TA METODA

