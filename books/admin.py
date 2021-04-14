from django.contrib import admin
from books.models import Book, Loan, LoanAmount

# Register your models here.
admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(LoanAmount)

