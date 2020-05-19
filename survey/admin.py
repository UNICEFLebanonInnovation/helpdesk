from django.contrib import admin
from reversion.admin import VersionAdmin
from suit.admin import RelatedFieldAdmin, get_related_field
from import_export import resources, fields
from import_export import fields
from import_export.admin import ImportExportModelAdmin

from survey.models import LASER, Map, Research
from survey.forms import ResearchForm


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


@admin.register(LASER)
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


@admin.register(Research)
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


@admin.register(Map)
class MapAdmin(ImportExportModelAdmin):
    resource_class = MapResource

    list_display = ('name', 'description', 'status')
    date_hierarchy = 'created'
    list_filter = ('status', )
