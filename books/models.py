from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

class Book(models.Model):
    title =models.CharField(_("title"), max_length=100)
    description = RichTextField()
    author = models.CharField(_("author"),max_length=100)
    image = models.ImageField(_("image"), upload_to='cover/',blank=True )
    price = models.PositiveIntegerField(_("price"))
    active = models.BooleanField(_("active"), default=True)
    date_time_created = models.DateTimeField(_("date time created"), auto_now_add=True)
    date_time_modified = models.DateTimeField(_("date time modified"), auto_now=True)

    class Meta:
        verbose_name = _('books')
        verbose_name_plural = _('books')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("books:book_detail", args=[self.id])
    
class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    email = models.EmailField(_("email"), max_length=254)
    text = models.TextField(_("text comment"))
    active = models.BooleanField(_("active"), default=True)
    date_time_created = models.DateTimeField(_("date time created"), auto_now_add=True)
    date_time_modified = models.DateTimeField(_("date time modified"), auto_now=True)

    class Meta:
        verbose_name = _('comments')
        verbose_name_plural = _('comments')