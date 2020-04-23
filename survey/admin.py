from django.contrib import admin
from reversion.admin import VersionAdmin
from suit.admin import RelatedFieldAdmin, get_related_field
from import_export import resources, fields
from import_export import fields
from import_export.admin import ImportExportModelAdmin

from survey.models import LASER


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

