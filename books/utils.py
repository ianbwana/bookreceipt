from django.utils import timezone
import datetime
from .models import Loan

def update_loan_prices():
    story_two_days = timezone.localtime(timezone.now()) + datetime.timedelta(days=-2)
    story_three_days = timezone.localtime(timezone.now()) + datetime.timedelta(days=-3)
    Loan.objects.filter(
        status="active", user__user_profile__story="story one"
    ).update(amount=1)
    Loan.objects.filter(
        status="active", user__user_profile__story="story two", book__book_type__in=["novel", "regular"]
    ).update(amount=1.5)
    Loan.objects.filter(
        status="active", user__user_profile__story="story two", book__book_type="novel"
    ).update(amount=3)
    Loan.objects.filter(
        status="active", user__user_profile__story="story three", start_date__gt=story_two_days, book__book_type="regular"
    ).update(amount=1.5)
    Loan.objects.filter(
        status="active", user__user_profile__story="story three", start_date__gt=story_three_days, book__book_type="novel"
    ).update(amount=1.5)
    # print("Prices updated for date {}".format(datetime.datetime.utcnow().strftime("%m/%d/%Y")))