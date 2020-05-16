from django.views.generic.base import TemplateView
from .models import Map


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        maps = Map.objects.all()

        return {
            'maps': maps
        }
