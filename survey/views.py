from django.views.generic.base import TemplateView
from django_filters.views import FilterView
from django.db.models import F, Q, Sum, Count
from json_tag import dumps
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableView
from django_tables2.export.views import ExportMixin

from .models import Map, Research, KnowledgeTracker
from .tables import  KnowledgeTrackerTable
from .filters import KnowledgeTrackerFilter


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        maps = Map.objects.all()

        return {
            'maps': maps
        }


class MapsView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        items = Map.objects.all()

        return {
            'maps': items
        }


class ResearchesView(TemplateView):
    template_name = 'researches.html'

    def get_context_data(self, **kwargs):
        items = Research.objects.all()

        return {
            'items': items
        }


class KnowledgeTrackerList(
    FilterView,
    ExportMixin,
    SingleTableView,
    RequestConfig):
    table_class = KnowledgeTrackerTable
    model = KnowledgeTracker
    template_name = 'dashboard_kmtracker.html'
    table = KnowledgeTrackerTable(KnowledgeTracker.objects.all(), order_by='issue_number')

    filterset_class = KnowledgeTrackerFilter

    def get_queryset(self):
        return KnowledgeTracker.objects.all().order_by('issue_number')


class KnowledgeTrackerChartsView(TemplateView):
    template_name = 'charts.html'

    def get_context_data(self, **kwargs):

        instances = KnowledgeTracker.objects.all()

        total_validated_by_ttc = instances.filter(validated_by_technical_committee=True).count()
        total_validated_by_moph = instances.filter(validated_by_moph=True).count()

        category_data = KnowledgeTracker.objects.all() \
            .values('issue_category') \
            .annotate(name=F('issue_category'), y=Count('issue_category')) \
            .order_by('issue_category') \
            .values('issue_category', 'y')

        category_data = dumps(category_data)

        target_data = KnowledgeTracker.objects.all() \
            .values('target_population') \
            .annotate(name=F('target_population'), y=Count('target_population')) \
            .order_by('target_population') \
            .values('target_population', 'y')

        target_data = dumps(target_data)

        source_data = KnowledgeTracker.objects.all() \
            .values('source') \
            .annotate(name=F('source'), y=Count('source')) \
            .order_by('source') \
            .values('source', 'y')

        source_data = dumps(source_data)

        return {
            'total': instances.count(),
            'total_validated_by_ttc': total_validated_by_ttc,
            'total_validated_by_moph': total_validated_by_moph,
            'category_data': category_data,
            'target_data': target_data,
            'source_data': source_data
        }
