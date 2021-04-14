from __future__ import absolute_import, unicode_literals

from celery import shared_task
from books.utils import update_loan_prices
# from celery import task

@shared_task()
def update_loan_amounts():
    return update_loan_prices()