from __future__ import unicode_literals

import os
import pathlib
import uuid as uuid

from colorful.fields import RGBColorField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, UUIDField
from django.dispatch import receiver
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from imagekit.utils import get_cache

from jurycore.helpers.slug_helper import unique_slugify


class Booklet(models.Model):
    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)
    session_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.session_name

    def save(self, *args, **kwargs):
        slug_str = slugify(self.session_name)
        unique_slugify(self, slug_str)
        super(Booklet, self).save(*args, **kwargs)


class Delegate(models.Model):
    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)
    booklet = models.ForeignKey("Booklet", on_delete=CASCADE)
    name = models.CharField(max_length=100)

    def get_upload_path(self, filename):
        return os.path.join("delegate_pictures", self.booklet.slug, "%s%s" % (self.uuid, pathlib.Path(filename).suffix))

    photo = models.ImageField(upload_to=get_upload_path)
    photo_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(250, 250)],
                                     format='JPEG',
                                     options={'quality': 60})
    photo_print = ImageSpecField(source='photo',
                                 processors=[ResizeToFill(300, 400)],
                                 format='JPEG',
                                 options={'quality': 100})
    committee = models.ForeignKey("Committee", on_delete=CASCADE)
    delegation = models.ForeignKey("Delegation", on_delete=CASCADE)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return "%s (%s, %s)" % (self.name, self.committee.name, self.delegation.name)


@receiver(models.signals.post_delete, sender=Delegate)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding Delegate object is deleted.
    """

    if not instance.pk:
        return False

    # Delete thumbnails
    for field in ['photo_thumbnail', 'photo_print']:
        field = getattr(instance, field)
        try:
            file = field.file
        except FileNotFoundError:
            pass
        else:
            cache_backend = field.cachefile_backend
            cache_backend.cache.delete(cache_backend.get_key(file))
            field.storage.delete(file.name)
    # Delete original photo
    instance.photo.delete(save=False)


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

    # Check if photo changed
    new_file = instance.photo
    if not old_file == new_file:
        old_instance = Delegate.objects.get(pk=instance.pk)

        # Delete thumbnails
        for field in ['photo_thumbnail', 'photo_print']:
            field = getattr(old_instance, field)
            try:
                file = field.file
            except FileNotFoundError:
                pass
            else:
                cache_backend = field.cachefile_backend
                cache_backend.cache.delete(cache_backend.get_key(file))
                field.storage.delete(file.name)
        # Delete original photo
        old_instance.photo.delete(save=False)
        # Clear cache
        # necessary because the name of the thumbnails change
        # and the cache still points to the old (and now deleted) photos
        get_cache().clear()

class Delegation(models.Model):
    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    colour = RGBColorField(blank=True)
    booklet = models.ForeignKey("Booklet", on_delete=CASCADE)

    def __str__(self):
        return self.name


class Committee(models.Model):
    uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    booklet = models.ForeignKey("Booklet", on_delete=CASCADE)

    def __str__(self):
        return self.name
