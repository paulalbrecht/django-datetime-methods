from django.shortcuts import render
from django.db.models import F, ExpressionWrapper, fields
from django.db.models import CharField, Case, Value, When
from django.utils import timezone
from datetime import timedelta

from .models import Activity


def activity_list(request):
    now = timezone.now()
    objects = Activity.objects.all().order_by('-due_date')
    for o in objects:
        overdue = now - o.due_date
        days = overdue.days
        if days <= 25:
            o.overdue = 'GREEN'
        elif 25 < days < 75:
            o.overdue = 'YELLOW'
        else:
            o.overdue = 'RED'

    return render(request, 'activities/activity_list.html', {
        'object_list': objects
    })


def activity_tag(request):
    objects = Activity.objects.all().order_by('-due_date')
    return render(request, 'activities/activity_tag.html', {
        'object_list': objects
    })


def activity_expression(request):
    overdue = ExpressionWrapper(timezone.now() - F('due_date'), output_field=fields.DurationField())
    objects = Activity.objects.all().order_by('-due_date').annotate(overdue=overdue)
    return render(request, 'activities/activity_expression.html', {
        'object_list': objects
    })


def activity_casewhen(request):
    green_date = timezone.now() - timedelta(days=25)
    yellow_date = timezone.now() - timedelta(days=75)
    objects = Activity.objects.all().order_by('-due_date').annotate(
        overdue=Case(
            When(due_date__gte=green_date, then=Value('GREEN')),
            When(due_date__gt=yellow_date, then=Value('YELLOW')),
            default=Value('RED'),
            output_field=CharField(),))
    return render(request, 'activities/activity_casewhen.html', {
        'object_list': objects
    })
