from django.db import models
from datetime import datetime

class Subscription(models.Model):
    amount = models.DecimalField("amount", decimal_places=2, max_digits=6)
    payDay = models.DateField('Date', default=datetime.now)
    icon = models.ImageField('icon', upload_to='images/')


    def __str__(self):
        return f'Подписка {self.receiver}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписка'
