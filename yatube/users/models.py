from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Password(models.Model):
    passw = models.CharField('Password', max_length=200)
    new_passw1 = models.CharField('New password', max_length=200)
    new_passw2 = models.CharField('Repet your password', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Password'
