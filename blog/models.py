from django.db import models
from django.db.models.enums import Choices, TextChoices
from django.db.models.expressions import OrderBy
from django.utils.translation import gettext_lazy as _
from django.conf import settings


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("title"))
    active = models.BooleanField(verbose_name=_("active"))

    class Meta:
        db_table = 'Category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):

    class statusChoise(models.TextChoices):
        DRAFT = _("draft")
        PUBLISHED = _("published")

    title = models.CharField(verbose_name=_("title"), max_length=50)
    slug = models.SlugField(verbose_name=_("slug"), max_length=50, allow_unicode=True, unique_for_date='publish_time')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    lead = models.CharField(verbose_name=_("lead"), max_length=50, null=True, blank=True)
    body = models.CharField(verbose_name=_("body"), max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
    featured = models.BooleanField(verbose_name=_("featured") , null=True)
    created = models.DateField(verbose_name=_("created"), auto_now=False, auto_now_add=True)
    updated = models.DateField(verbose_name=_("updated"), auto_now=True, auto_now_add=False)
    status = models.CharField(verbose_name=_("status"), max_length=15 , choices=statusChoise.choices, default=statusChoise.DRAFT)
    publish_time = models.DateField(verbose_name=_("publish_time"), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Post'
        managed = True
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ['-publish_time']
