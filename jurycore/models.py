from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Delegate(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='delegate_pictures/')
    committee = models.ForeignKey("Committee")
    delegation = models.ForeignKey("Delegation")
    remarks = models.TextField(blank = True)

    def __str__(self):              # __unicode__ on Python 2
        return "(%s, %s)" % (self.committee.name, self.delegation.name)


class Delegation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Committee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
