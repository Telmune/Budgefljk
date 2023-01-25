from datetime import datetime

from django.db import models

from category.models import Category


class Transaction(models.Model):
    receiver = models.CharField('receiving', max_length=100)
    amount = models.DecimalField("balance", decimal_places=2, max_digits=6)
    date = models.DateField('Date', default=datetime.now)
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f'Транзакция {self.receiver}'

    class Meta:
            verbose_name = 'Транзакция'
            verbose_name_plural = 'Транзакция'