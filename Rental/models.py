from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import  User
from shelf.models import BookItem
#from django.conf import settings
from django.utils.timezone import now

class Rental (models.Model):
  #  who = models.ForeignKey(settings.AUTH_USER_MODEL)

    who = models.ForeignKey(User)
    what = models.ForeignKey(BookItem)
    when = models.DateTimeField(default=now)
    returned = models.DateTimeField(null=True, blank=True)
    #To pole moze puste przy wysylaniu

    def __str__(self):
        return '' #zaddom
