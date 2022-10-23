from __future__ import absolute_import, unicode_literals

from celery import shared_task
from datetime import datetime

@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task(name="print_msg_main")
def print_message(message, *args, **kwargs):
    print(f"Celery is working!! Message is {message}")


@shared_task(name="print_time")
def print_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Current Time is {current_time}")


@shared_task(name='get_calculation')
def calculate(val1, val2):
    total = val1 + val2
    return total