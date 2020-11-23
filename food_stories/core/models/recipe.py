from django.db import models
from autoslug import AutoSlugField

from .category import Category


class Recipe(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title', unique=True)
    note = models.CharField(max_length=100, verbose_name='Short description')
    body = models.TextField()
    featured_img = models.ImageField()
    category = models.ManyToManyField(Category)
    slug = AutoSlugField(populate_from='title', null=True)

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
    
    def __str__(self):
        return self.title