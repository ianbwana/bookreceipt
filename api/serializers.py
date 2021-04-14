from accounts.models import Profile, LibraryUser
from books.models import Book, Loan, LoanAmount
from rest_framework import serializers
from django.db.models import Sum
from decimal import Decimal as D
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class LibraryUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = LibraryUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = '__all__'


class LoanAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanAmount
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField()
    borrowed_books = serializers.SerializerMethodField()
    loan_total = serializers.SerializerMethodField()

    def get_user_info(selfs, Profile):
        info = LibraryUser.objects.filter(
            user_profile=Profile).values('id', 'username', 'first_name', 'last_name', 'email'
                                         )
        return info

    def get_loan_total(selfs, Profile):
        total = LoanAmount.objects.filter(loan__user__user_profile=Profile).aggregate(sum=Sum('amount'))
        return total["sum"]

    def get_borrowed_books(self, Profile):
        loans = Loan.objects.filter(user__user_profile=Profile).values()
        return loans

    class Meta:
        model = Profile
        fields = ('user', 'borrowed_books', 'story', 'loan_total', 'user_info')
        # depth = 1