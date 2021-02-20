import json
import datetime
from django import template
from datetime import date
from survey.models import LASER, KnowledgeTracker
from django.db.models import Sum

register = template.Library()


@register.simple_tag
def get_dashboard_number(name):
    if name == 'total':
        return KnowledgeTracker.objects.all().count()
    if name == 'link':
        return KnowledgeTracker.objects.filter(relevant_link__isnull=False).count()
    if name == 'validated_by_moph':
        return KnowledgeTracker.objects.filter(validated_by_moph=True).count()
    if name == 'validated_by_technical_committee':
        return KnowledgeTracker.objects.filter(validated_by_technical_committee=True).count()
    if name == 'validated_by_both':
        return KnowledgeTracker.objects.filter(validated_by_moph=True, validated_by_technical_committee=True).count()

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
