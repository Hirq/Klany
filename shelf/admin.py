#coding: utf-8

from __future__ import unicode_literals, absolute_import

#####################################

from .models import  Author, Publisher, Book

from django.contrib import admin


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name','first_name']
    ordering =['last_name']



class BookAdmin(admin.ModelAdmin):
    search_fields =  ['title']
    list_display =  ['title','author','isbn','publisher']

admin.site.register(Book, BookAdmin)

##PIERW MODEL, POTEM KLASA ADMINISTRUJACA
admin.site.register(Author, AuthorAdmin)

admin.site.register(Publisher)
#rejestrowanie na poczatek w nawiasach[] potem przejscie na to wyzej
#admin.site.register([Publisher,Book])