from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from mezzanine.pages.models import RichTextPage
from mezzanine.generic.fields import CommentsField


class PageComments(models.Model):
    page = models.OneToOneField(RichTextPage)
    comments = CommentsField()

    def get_absolute_url(self):
        return self.page.get_absolute_url()

@receiver(post_save, sender=RichTextPage)
def update_pagecomments(sender, instance, **kwargs):
     if instance.allow_comments:
        PageComments.objects.get_or_create(page=instance)
