import json
import datetime
from django import template
from datetime import date
from survey.models import LASER, Research
from django.db.models import Sum

register = template.Library()


@register.simple_tag
def get_dashboard_number(name):

    if name == 'total':
        return Research.objects.all().count()
    if name == 'link':
        return Research.objects.filter(report_link__isnull=False).count()
    if name == '2020':
        return Research.objects.filter(publication_year='2020').count()
    if name == 'National':
        return Research.objects.filter(geographical_coverage='National').count()

    return 0


@register.simple_tag
def get_dashboard_number_1(name):

    if name == 'total':
        return LASER.objects.all().count()
    if name == 'link':
        return LASER.objects.filter(report_link__isnull=False).count()
    if name == 'cost':
        return LASER.objects.all().aggregate(estimated_cost=Sum('estimated_cost'))
    if name == 'planned':
        return LASER.objects.filter(status='Planned').count()
    if name == 'ongoing':
        return LASER.objects.filter(status='Ongoing').count()
    if name == 'national_focus':
        return LASER.objects.filter(geographical_focus='National').count()
    if name == 'planned_list':
        return LASER.objects.filter(status='Planned').exclude(organization__isnull=True).order_by('-created')
    if name == 'ongoing_list':
        return LASER.objects.filter(status='Ongoing').exclude(organization__isnull=True).order_by('-created')

    return 0
