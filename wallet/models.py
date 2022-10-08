from django.db import models
from users.models import CustomUser

# Create your models here.


class Wallet(models.Model):
    name = models.CharField(max_length=32, unique=False)
    amount = models.IntegerField(default=0)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Log(models.Model):
    TYPES = [
        ('p', 'positive'),
        ('n', 'negative')
    ]
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    description = models.CharField(max_length=256, null=True, blank=True)
    log_type = models.CharField(choices=TYPES, max_length=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wallet.name
