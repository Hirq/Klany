from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import  User
from shelf.models import BookItem
from django.conf import settings
from django.utils.timezone import now
from django.core.urlresolvers import reverse

class Rental (models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)

    name = models.CharField(max_length=40, default=' ')
    whoo = models.CharField(max_length=40, default=' ')

    # who = models.ForeignKey(User,default='')
    # what = models.ForeignKey(BookItem)
    # when = models.DateTimeField(default=now)
    # returned = models.DateTimeField(null=True, blank=True)
    #To pole moze puste przy wysylaniu

   # def __str__(self):

     # return '' #zaddom
    def __str__(self):
        return "{name} {whoo} {who}".format(name=self.name, whoo=self.whoo, who=self.who)

    def get_absolute_url(self):
        return "List"
        # return "List/%i/" % self.id

