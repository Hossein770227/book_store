from django.db import models
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    title =models.CharField(_("title"), max_length=100)
    description = models.TextField(_("description"))
    author = models.CharField(_("author"),max_length=100)
    price = models.PositiveIntegerField(_("price"))
    active = models.BooleanField(_("active"), default=True)
    date_time_created = models.DateTimeField(_("date time created"), auto_now_add=True)
    date_time_modified = models.DateTimeField(_("date time modified"), auto_now=True)

    class Meta:
        verbose_name = _('books')
        verbose_name_plural = _('books')

    def __str__(self):
        return self.title

