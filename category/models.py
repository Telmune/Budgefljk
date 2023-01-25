from datetime import datetime

from django.db import models


class Category(models.Model):
    title = models.CharField('title', max_length=100)
    color = models.CharField('Color', max_length=100)
    icon = models.ImageField('icon', upload_to='images/')

    def __str__(self):
        return f'Категория {self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'


