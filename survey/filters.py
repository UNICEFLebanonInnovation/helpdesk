from django.utils.translation import ugettext as _

from django_filters import (
    FilterSet,
    ModelChoiceFilter,
    DateRangeFilter,
    DateFromToRangeFilter,
    DateFilter,
    CharFilter,
    ChoiceFilter
)

from .models import KnowledgeTracker


class KnowledgeTrackerFilter(FilterSet):

    class Meta:
        model = KnowledgeTracker
        fields = {
            'issue_description': ['icontains'],
            'answer': ['icontains'],
            'reported_by': ['exact'],
            'issue_category': ['exact'],
            'target_population': ['exact'],
            'source': ['exact'],
            'validated_by_technical_committee': ['exact'],
            # 'validated_by_moph': ['exact'],
        }
