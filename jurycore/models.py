from __future__ import unicode_literals

from django.db import models
from django.db.models import CASCADE;


# Create your models here.

class Booklet(models.Model):
    session_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()

    def __str__(self):
        return self.session_name

    class Meta:
        permissions = (
            ('view_booklet', 'Can view booklet'),
        )


class Delegate(models.Model):
    booklet = models.ForeignKey("Booklet", on_delete=CASCADE)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='delegate_pictures/')
    committee = models.ForeignKey("Committee", on_delete=CASCADE)
    delegation = models.ForeignKey("Delegation", on_delete=CASCADE)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return "(%s, %s)" % (self.committee.name, self.delegation.name)

    class Meta:
        permissions = (
            ('view_delegate', 'Can view delegate'),
        )


class Delegation(models.Model):
    name = models.CharField(max_length=100)
    colour = models.CharField(max_length=8, blank=True)
    booklet = models.ForeignKey("Booklet", on_delete=CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        permissions = (
            ('view_delegation', 'Can view delegation'),
        )


class Committee(models.Model):
    name = models.CharField(max_length=100)
    booklet = models.ForeignKey("Booklet", on_delete=CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        permissions = (
            ('view_committee', 'Can view committee'),
        )
