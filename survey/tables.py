# coding: utf-8
import django_tables2 as tables

from .models import KnowledgeTracker


class BootstrapTable(tables.Table):
    class Meta:
        model = KnowledgeTracker
        template = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-bordered table-striped table-hover'}
        fields = ()


class KnowledgeTrackerTable(BootstrapTable):
    link_column = tables.TemplateColumn(verbose_name='Related Link', orderable=False,
                                        template_name='django_tables2/link_column.html')

    feedback_column = tables.TemplateColumn(verbose_name='Related Link', orderable=False,
                                        template_name='django_tables2/feedback_column.html')

    source_link = tables.TemplateColumn(verbose_name='Related Link', orderable=False,
                                        template_name='django_tables2/link_column.html')
    # validated_by_moph_column = tables.TemplateColumn(verbose_name='Validated by MOPH', orderable=False,
    #                                                  template_name='django_tables2/validated_by_moph_column.html')
    validated_by_ttc_column = tables.TemplateColumn(verbose_name='Validated by Technical Committee', orderable=False,
                                                     template_name='django_tables2/validated_by_ttc_column.html')

    template = 'django_tables2/bootstrap.html'

    class Meta:
        model = KnowledgeTracker
        fields = (
            'issue_number',
            'high_priority',
            'feedback_column',
            'reported_by__last_name',
            'issue_category',
            'issue_description',
            'source',
            'source_link',
            'source_number_percentage',
            'frequency',
            'target_population',
            'other_population_considerations'
            'answer',
            'validated_by_ttc_column',
            # 'validated_by_moph_column',
            'dissemination_method_list',
            'link_column',
        )
