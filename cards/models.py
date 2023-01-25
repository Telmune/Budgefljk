from django.db import models


class BankCard(models.Model):
    cardHolder = models.CharField('Владелец карточки', max_length=100)
    expirationDate = models.DateField('Дата истечения срока', max_length=100)
    balance = models.DecimalField('Баланс', decimal_places=2, max_digits=6)
    lastFourDigigts = models.PositiveIntegerField('Последние четыре цыфры', default=0)

    def __str__(self):
        return f'Карта {self.cardHolder}'

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карта'

class Goal(models.Model):
    goal = models.CharField('Цель', max_length=100)
    budget = models.DecimalField('Бюджет', decimal_places=2, max_digits=6)
    date = models.DateField('Дата')


    def __str__(self):
        return f'Цель {self.goal}'

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цель'