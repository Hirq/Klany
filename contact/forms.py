from __future__ import unicode_literals
from .models import Message
from django import  forms



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name','email','message')



class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())