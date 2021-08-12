from django.views.generic.base import TemplateView
from django_filters.views import FilterView
from django.db.models import F, Q, Sum, Count
from json_tag import dumps
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableView
from django_tables2.export.views import ExportMixin

from .models import Map, Research, KnowledgeTracker
from .tables import  KnowledgeTrackerTable
from .filters import KnowledgeTrackerFilter
from django.http import HttpResponse, JsonResponse
from django.db.models import F
from django.db.models.functions import TruncMonth

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
        total_high_priority = instances.filter(high_priority=True).count()
        # total_validated_by_moph = instances.filter(validated_by_moph=True).count()

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
            .values('name', 'y')

        target_data = dumps(target_data)

        source_data = KnowledgeTracker.objects.all() \
            .values('source') \
            .annotate(name=F('source'), y=Count('source')) \
            .order_by('source') \
            .values('name', 'y')

        source_data = dumps(source_data)


        organization_data = KnowledgeTracker.objects.all() \
            .values('reported_by__last_name') \
            .annotate(name=F('reported_by__last_name'), y=Count('reported_by__last_name')) \
            .order_by('reported_by__last_name') \
            .values('reported_by__last_name', 'y')

        organization_data = dumps(organization_data)

        # month_data = KnowledgeTracker.objects.all().annotate(
        #     year=created__year,
        #     month=created__month,
        # ).values('year', 'month').annotate(count=Count('id'))

        month_data= KnowledgeTracker.objects.values(
            month=TruncMonth('created')
        ).annotate(
            count=Count('id')
        ).order_by('month')

        finalMonthData = []


        for monthRecord in month_data:
        #    # strftime("%Y-%m")
            month = monthRecord['month'].strftime("%Y-%m")
            recordCount = monthRecord['count']
            finalMonthData.append({"month":month, "y":recordCount})

        print('----------------------------------------------------------------------------------------')

        print(finalMonthData)
        print('----------------------------------------------------------------------------------------')
        month_data = dumps(finalMonthData)


        print(month_data)

        return {
            'total': instances.count(),
            'total_validated_by_ttc': total_validated_by_ttc,
            'total_high_priority': total_high_priority,
            # 'total_validated_by_moph': total_validated_by_moph,
            'category_data': category_data,
            'target_data': target_data,
            'source_data': source_data,
            'organization_data': organization_data,
            'month_data' : month_data
        }


def FeedbackSelectView(request):
    feedback_id = request.POST['record_id']
    result = {'result': False}
    can_edit= False
    try:

        qs = KnowledgeTracker.objects.get(id=feedback_id)

        if qs:
            result['result'] = True
            result['feedback_status'] = qs.feedback_status
            result['feedback_text'] = qs.feedback_text
            result['feedback_color'] = qs.feedback_color
            if (request.user.id == qs.created_by.id):
                can_edit = True
            else:
                can_edit= False

            result['can_edit'] = can_edit


    except KnowledgeTracker.DoesNotExist:
        pass


    return JsonResponse(result)



def FeedbackUpdateView(request):

    feedback_id = request.POST['record_id']
    feedback_status = request.POST['feedback_status']
    feedback_text = request.POST['feedback_text']
    feedback_color = request.POST['feedback_color']

    result = {'result': False}

    try:

        feedback = KnowledgeTracker.objects.get(id=feedback_id)
        feedback.feedback_status = feedback_status
        feedback.feedback_text = feedback_text
        feedback.feedback_color = feedback_color
        feedback.save()

        result['result'] = True


    except KnowledgeTracker.DoesNotExist:
        pass

    return JsonResponse(result)
