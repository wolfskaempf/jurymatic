from __future__ import unicode_literals

import uuid as uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, UUIDField
from django.utils.text import slugify

from jurycore.helpers.slug_helper import unique_slugify


class Booklet(models.Model):
    session_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.session_name

    def save(self, *args, **kwargs):
        slug_str = slugify(self.session_name)
        unique_slugify(self, slug_str)
        super(Booklet, self).save(*args, **kwargs)

    class Meta:
        permissions = (
            ('view_booklet', 'Can view booklet'),
        )


class Delegate(models.Model):
    uuid = UUIDField(default=uuid.uuid4(), editable=False, unique=True)
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
    uuid = UUIDField(default=uuid.uuid4(), editable=False, unique=True)
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
    uuid = UUIDField(default=uuid.uuid4(), editable=False, unique=True)
    name = models.CharField(max_length=100)
    booklet = models.ForeignKey("Booklet", on_delete=CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        permissions = (
            ('view_committee', 'Can view committee'),
        )
