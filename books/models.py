from django.db import models
from decimal import Decimal as D
from django.conf import settings
# Create your models here.


class Book(models.Model):
    AVAILABLE = 'available'
    LOANED = 'loaned'
    BOOK_STATUS_CHOICES = (
        ('available', AVAILABLE),
        ('loaned', LOANED)
    )

    REGULAR = 'regular'
    FICTION = 'fiction'
    NOVEL = 'novel'
    BOOK_TYPE_CHOICES = (
        ('regular', REGULAR),
        ('fiction', FICTION),
        ('novel', NOVEL)
    )

    title = models.CharField(max_length=500)
    quantity = models.IntegerField()
    status = models.CharField(max_length=15, choices=BOOK_STATUS_CHOICES, null=True, blank=True)
    book_type = models.CharField(max_length=15, choices=BOOK_TYPE_CHOICES, null=True, blank=True, default=REGULAR)

    def __str__(self):
        return self.title


class Loan(models.Model):
    ACTIVE = 'active'
    REPAID = 'repaid'
    LOAN_STATUS_CHOICES = (
        ('active', ACTIVE),
        ('repaid', REPAID)
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_loans', on_delete=models.DO_NOTHING)
    book = models.ForeignKey('books.Book', related_name='book', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=LOAN_STATUS_CHOICES, default=ACTIVE)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class LoanAmount(models.Model):
    loan = models.ForeignKey('books.Loan', related_name='loan', on_delete=models.CASCADE)
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        default=D("1.00"),
        null=True
    )
    date_created = models.DateTimeField(auto_now_add=True)
