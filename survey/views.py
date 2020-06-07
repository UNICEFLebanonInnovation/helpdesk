from django.views.generic.base import TemplateView
from .models import Map, Research


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