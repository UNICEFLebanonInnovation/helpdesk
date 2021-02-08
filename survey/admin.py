from django.contrib import admin
from reversion.admin import VersionAdmin
from suit.admin import RelatedFieldAdmin, get_related_field
from import_export import resources, fields
from import_export import fields
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin

from survey.models import LASER, Map, Research, InfoTracker
from survey.forms import ResearchForm, InfoTrackerForm
from .utils import has_group


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


class InfoTrackerResource(resources.ModelResource):
    class Meta:
        model = InfoTracker
        fields = (
            'issue_number',
            'issue_description',
            'reported_by',
            'answer',
            'validated_by_technical_committee',
            'validated_by_moph',
            'dissemination_method',
            'relevant_link',
        )
        export_order = fields


@admin.register(InfoTracker)
class InfoTrackerAdmin(ExportActionModelAdmin, VersionAdmin):
    resource_class = InfoTracker
    form = InfoTrackerForm
    list_display = (
            'issue_number',
            'issue_description',
            'reported_by',
            'answer',
            'validated_by_technical_committee',
            'validated_by_moph',
            'dissemination_method',
            'relevant_link',
        )
    date_hierarchy = 'created'
    list_filter = ('validated_by_technical_committee', 'validated_by_moph')
    search_fields = (
        'issue_description',
        'reported_by',
        'answer',
        'dissemination_method'
    )
    readonly_fields = (
        'issue_number',
    )

    fieldsets = [
        ('Issue details', {
            'fields': [
                'issue_number',
                'issue_description',
                'reported_by'
            ]
        }),
        ('Response', {
            'fields': [
                'answer',
                'validated_by_technical_committee',
                'validated_by_moph',
                'dissemination_method',
                'relevant_link',
            ]
        })
    ]

    def get_readonly_fields(self, request, obj=None):

        fields = [
            'issue_number',
            'issue_description',
            'reported_by',
            'answer',
            'validated_by_technical_committee',
            'validated_by_moph',
            'dissemination_method',
            'relevant_link',
        ]

        if has_group(request.user, 'UNICEF'):
            fields = [
                'issue_number',
            ]

        if has_group(request.user, 'NON_UNICEF'):
            fields = [
                'issue_number',
                'answer',
                'validated_by_technical_committee',
                'validated_by_moph',
                'dissemination_method',
                'relevant_link',
            ]

        return fields
