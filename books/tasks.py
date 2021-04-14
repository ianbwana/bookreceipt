from __future__ import absolute_import, unicode_literals

from celery import shared_task
# from celery import task

@shared_task()
def update_loan_amounts():
    # update_loan_prices()
    print('test beat')