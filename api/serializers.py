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
        fields = ('id',)


class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = '__all__'


class LoanAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanAmount
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = LibraryUserSerializer()
    borrowed_books = serializers.SerializerMethodField()

    def get_borrowed_books(self, Profile):
        loans = Loan.objects.filter(user__user_profile=Profile).values()
        return loans

    class Meta:
        model = Profile
        fields = ('user', 'borrowed_books', 'story')
        depth = 1