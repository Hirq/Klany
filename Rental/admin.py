#coding: utf-8

from __future__ import unicode_literals, absolute_import

#####################################

from .models import  Rental

from django.contrib import admin


class RentalAdmin(admin.ModelAdmin):
    search_fields = ['name,''whoo']
    #,'what','when','returned'
    # ordering =['who']

admin.site.register(Rental, RentalAdmin)


##PIERW MODEL, POTEM KLASA ADMINISTRUJACA
