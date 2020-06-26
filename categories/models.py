from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.shortcuts import reverse
from django_countries.fields import CountryField


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,
                            max_length=50,
                            help_text='Unique value for product page URL, created from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords",
                                     max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description",
                                        max_length=255,
                                        help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'ProductCategories'
        ordering = ['category_name']
        verbose_name_plural = 'ProductCategories'

    def get_absolute_url(self):
        return reverse('categories:categoryView', kwargs={'slug': self.slug})