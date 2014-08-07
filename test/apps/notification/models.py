# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime


class NotificationType(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "%s" % (self.name,)


class Notification(models.Model):
    to = models.ForeignKey(User, blank=True, null=True, related_name='to')
    type = models.ForeignKey(NotificationType, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    body = models.TextField(max_length=3000, blank=True, null=True)
    url_image = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=300, blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    readed = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s" % (self.title,)
