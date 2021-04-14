from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import LoanAmount, Loan


@receiver(post_save, sender=Loan)
def create_loan_amount(sender, instance, created=False, **kwargs):
    print("Loan created/altered")
    try:
        amount = instance.amount
        LoanAmount.objects.create(loan=instance, amount=amount)
        print("amount added")
    except Exception as e:
        print("{}".format(e))