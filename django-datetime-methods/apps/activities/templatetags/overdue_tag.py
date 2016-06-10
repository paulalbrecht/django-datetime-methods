from __future__ import unicode_literals
# from datetime import timedelta
from django.utils import timezone

from django import template

register = template.Library()


@register.simple_tag
def get_activity_overdue(due_date):
    now = timezone.now()
    overdue = now - due_date
    days = overdue.days
    if days <= 25:
        return 'GREEN'
    elif 25 < days < 75:
        return 'YELLOW'
    else:
        return 'RED'
