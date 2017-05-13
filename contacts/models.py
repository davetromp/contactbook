# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    firstname = models.CharField(default=None, db_index=True, blank=True, null=True, max_length=255)
    lastname = models.CharField(default=None, db_index=True, blank=True, null=True, max_length=255)
    street = models.CharField(default=None, db_index=True, blank=True, null=True, max_length=255)
    zipcode = models.CharField(default=None, db_index=True, blank=True, null=True, max_length=255)
    city = models.CharField(default=None, db_index=True, blank=True, null=True, max_length=255)
    image_url = models.CharField(default=None, db_index=True, blank=True, null=True, max_length=255)
    thumbnail = models.TextField(default=None, db_index=True, blank=True, null=True)

    def __unicode__(self):
        return self.firstname + " " + self.lastname
