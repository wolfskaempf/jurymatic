from __future__ import unicode_literals

import os
import uuid as uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, UUIDField
from django.dispatch import receiver
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
    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)
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


@receiver(models.signals.post_delete, sender=Delegate)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding Delegate object is deleted.
    """
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


@receiver(models.signals.pre_save, sender=Delegate)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding Delegate object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Delegate.objects.get(pk=instance.pk).photo
    except Delegate.DoesNotExist:
        return False

    new_file = instance.photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class Delegation(models.Model):
    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)
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
    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    booklet = models.ForeignKey("Booklet", on_delete=CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        permissions = (
            ('view_committee', 'Can view committee'),
        )
