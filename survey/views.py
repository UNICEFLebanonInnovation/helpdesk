from django.views.generic.base import TemplateView
from django_filters.views import FilterView
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