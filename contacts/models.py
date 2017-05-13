# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    firstname = models.CharField(db_index=True, max_length=255)
    lastname = models.CharField(db_index=True, max_length=255)
    street = models.CharField(db_index=True, max_length=255)
    zipcode = models.CharField(db_index=True, max_length=255)
    city = models.CharField(db_index=True, max_length=255)
    image_url = models.CharField(db_index=True, max_length=255)
    thumbnail = models.TextField()

    def __unicode__(self):
        return self.firstname + " " + self.lastname
