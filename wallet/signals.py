from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Log


@receiver(post_save, sender=Log)
def update_wallet_amount(sender, instance, created, **kwargs):
    if created:
        wallet = instance.wallet
        log_type = instance.log_type
        init_amount = wallet.amount
        entry_amount = instance.amount
        if log_type == 'p':
            wallet.amount = int(init_amount) + int(entry_amount)
        elif log_type == 'n':
            if init_amount > entry_amount:
                wallet.amount = int(init_amount) - int(entry_amount)
            else:
                wallet.amount = 0
        else:
            print('else')
        wallet.save()
