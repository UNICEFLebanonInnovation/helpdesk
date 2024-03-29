from django.contrib import admin
from reversion.admin import VersionAdmin
from suit.admin import RelatedFieldAdmin, get_related_field
from import_export import resources, fields
from import_export import fields
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin

from survey.models import LASER, Map, Research, KnowledgeTracker
from survey.forms import ResearchForm, KnowledgeTrackerForm
from .utils import has_group
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

class DisseminationMethodFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Dissemination Method'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'dissemination_method'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
                    ('Community Activity', 'Community Activity'),
                    ('Social Media', 'Social Media'),
                    # ('Training', 'Training'),
                    ('Official External Communication', 'Official External Communication'),
                )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value():
            return queryset.filter(
                dissemination_method__contains=self.value()
            )
        return queryset


class LASERResource(resources.ModelResource):
    class Meta:
        model = LASER
        fields = (
            'id',
            'laser_id',
            'organization',
            'focal_point_contact',
            'title',
            'description',
            'status',
            'population_targeted',
            'sectors_covered',
            'report_link',
            'required_followup',
            'published_date',
            'publication_date',
            'estimated_cost',
            'category',
            'evaluation_type',
            'geographical_focus',
            'UNSF_outcome',
            'section'
        )
        export_order = fields


# @admin.register(LASER)
class LASERAdmin(ImportExportModelAdmin):
    resource_class = LASERResource

    list_display = ('laser_id', 'organization', 'title', 'status',
                    'category', 'section')
    date_hierarchy = 'created'
    list_filter = ('organization', 'status', 'category', 'section')
    # suit_list_filter_horizontal = ('organization', 'status', 'category', 'section')
    # list_select_related = True


class ResearchResource(resources.ModelResource):
    class Meta:
        model = Research
        fields = (
            'research_id',
            'title',
            'publication_year'
            'organizations',
            'researchers',
            'type',
            'main_sector',
            'geographical_coverage',
            'description',
            'report_link',
            'recommendations',
            'planned_actions',
        )
        export_order = fields


# @admin.register(Research)
class ResearchAdmin(ImportExportModelAdmin, VersionAdmin):
    resource_class = ResearchResource
    form = ResearchForm
    list_display = ('research_id', 'title', 'publication_year',
                    'type', 'main_sector', 'geographical_coverage')
    date_hierarchy = 'created'
    list_filter = ('type', 'main_sector', 'geographical_coverage', 'publication_year')
    search_fields = (
        'research_id',
        'title',
        'organizations',
        'researchers'
    )
    readonly_fields = (
        'research_id',
    )

    fieldsets = [
        ('', {
            # 'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'research_id',
                'title',
                'publication_year',
                'organizations',
                'researchers',
            ]
        }),
        ('', {
            'fields': [
                'type',
                'main_sector',
                'geographical_coverage',
                'description',
                'report_link',
            ]
        }),
        ('', {
            'fields': [
                'recommendations',
            ]
        }),
        ('', {
            'fields': [
                'planned_actions',
            ]
        }),
        ('', {
            'fields': [
                'taken_actions',
            ]
        })
    ]


class MapResource(resources.ModelResource):
    class Meta:
        model = Map
        fields = (
            'id',
            'name',
            'description',
            'link',
            'status',
        )
        export_order = fields


# @admin.register(Map)
class MapAdmin(ImportExportModelAdmin):
    resource_class = MapResource

    list_display = ('name', 'description', 'status')
    date_hierarchy = 'created'
    list_filter = ('status', )


class KnowledgeTrackerResource(resources.ModelResource):
    class Meta:
        model = KnowledgeTracker
        fields = (
            'issue_number',
            'high_priority',
            # 'reported_by__first_name',
            'reported_by__last_name',
            'issue_category',
            'issue_description',
            'source',
            'source_relevant_link',
            'source_number_percentage',
            'frequency',
            'target_population',
            'other_population_considerations',
            'answer',
            'validated_by_technical_committee',
            'dissemination_method',
            'relevant_link',
            'feedback_status',
            'feedback_text',
            'feedback_color',
            'created'
        )
        export_order = fields


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


@admin.register(KnowledgeTracker)
class KnowledgeTrackerAdmin(ExportActionModelAdmin, VersionAdmin):
    resource_class = KnowledgeTrackerResource
    form = KnowledgeTrackerForm
    list_display = (
            'issue_number',
            'high_priority',
            'feedback',
            'reported_organization',
            'issue_category',
            'issue_description',
            'source',
            'source_relevant_link',
            'source_number_percentage',
            'frequency',
            'target_population',
            'other_population_considerations',
            'answer',
            'validated_by_technical_committee',
            # 'validated_by_moph',
            'dissemination_method',
            'relevant_link'
        )

    def feedback(self, obj):
        t = render_to_string("django_tables2/feedback_column.html", {'id': str(obj.id), 'feedback_color': str(obj.feedback_color)})
        return mark_safe(t)

    feedback.allow_tags = True

    date_hierarchy = 'created'

    list_filter = (
        'high_priority',
        ('reported_by__last_name', custom_titled_filter('Reported By')),
        'issue_category',
        'source',
        'target_population',
        'other_population_considerations',
        'validated_by_technical_committee',
        # 'validated_by_moph',
        # DisseminationMethodFilter
    )
    suit_list_filter_horizontal = (
        'high_priority',
        'reported_by__last_name',
        'issue_category',
        'source',
        'target_population',
        'other_population_considerations',
        'validated_by_technical_committee',
        # 'validated_by_moph',
        # DisseminationMethodFilter
    )
    search_fields = (
        'issue_number',
        'high_priority',
        # 'reported_by',
        'issue_category',
        'issue_description',
        # 'frequency',
        'source',
        'source_relevant_link',
        'target_population',
        'other_population_considerations',
        'answer',
        # 'validated_by_technical_committee',
        # 'validated_by_moph',
        'dissemination_method',
        'relevant_link',
    )
    readonly_fields = (
        'issue_number',
    )

    list_editable = [
        'frequency',
    ]

    fieldsets = [
        ('Issue details', {
            'fields': [
                'issue_number',
                'high_priority',
                # 'reported_by',
                'issue_category',
                'issue_description',
                'source',
                'source_relevant_link',
                'source_number_percentage',
                'frequency',
                'target_population',
                'other_population_considerations',
            ]
        }),
        ('Response', {
            'fields': [
                'answer',
                'validated_by_technical_committee',
                # 'validated_by_moph',
                'dissemination_method',
                'relevant_link',
            ]
        })
    ]

    def has_import_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    # def has_change_permission(self, request, obj=None):
    #     if has_group(request.user, 'EDITOR'):
    #         if obj and obj.created_by == request.user:
    #             return True
    #         return False
    #     return True

    def get_readonly_fields(self, request, obj=None):

        fields = [
            'issue_number',
            'high_priority',
            'reported_by',
            'issue_category',
            'issue_description',
            'source',
            'source_relevant_link',
            'source_number_percentage',
            'target_population',
            'other_population_considerations',
            'answer',
            'validated_by_technical_committee',
            # 'validated_by_moph',
            'dissemination_method',
            'relevant_link',
        ]

        if has_group(request.user, 'ADMIN'):
            fields = [
                'issue_number',
            ]

        if has_group(request.user, 'EDITOR'):
            if obj:
                if obj.created_by == request.user:
                    fields = [
                        'issue_number',
                        'answer',
                        'validated_by_technical_committee',
                        # 'validated_by_moph',
                        'dissemination_method',
                        'relevant_link',
                    ]
                else:
                    fields = [
                        'issue_number',
                        'high_priority',
                        'reported_by',
                        'issue_category',
                        'issue_description',
                        'source',
                        'source_relevant_link',
                        'source_number_percentage',
                        'target_population',
                        'other_population_considerations',
                        'answer',
                        'validated_by_technical_committee',
                        # 'validated_by_moph',
                        'dissemination_method',
                        'relevant_link',
                    ]
            else:
                fields = [
                    'issue_number',
                    'answer',
                    'validated_by_technical_committee',
                    # 'validated_by_moph',
                    'dissemination_method',
                    'relevant_link',
                ]

        if has_group(request.user, 'VIEW'):
            if obj:
                fields = [
                    'issue_number',
                    'high_priority',
                    'reported_by',
                    'issue_category',
                    'issue_description',
                    'source',
                    'source_relevant_link',
                    'source_number_percentage',
                    'target_population',
                    'other_population_considerations',
                    'answer',
                    'validated_by_technical_committee',
                    # 'validated_by_moph',
                    'dissemination_method',
                    'relevant_link',
                ]
            else:
                fields = [
                    'issue_number',
                    'answer',
                    'validated_by_technical_committee',
                    # 'validated_by_moph',
                    'dissemination_method',
                    'relevant_link',
                ]
        return fields


    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.reported_by = request.user
        else:
            obj.modified_by = request.user

        super(KnowledgeTrackerAdmin, self).save_model(request, obj, form, change)

    # def get_queryset(self, request):
    #     if has_group(request.user, 'EDITOR'):
    #         return KnowledgeTracker.objects.filter(created_by=request.user)
    #     return KnowledgeTracker.objects.all()
