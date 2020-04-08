from django.contrib import admin
from survey.models import LASER


@admin.register(LASER)
class LASERAdmin(admin.ModelAdmin):
    list_display = ('laser_id', 'organization', 'title', 'status',
                    'category', 'section')
    date_hierarchy = 'created'
    list_filter = ('organization', 'status', 'category', 'section')
    suit_list_filter_horizontal = ('organization', 'status', 'category', 'section')
    list_select_related = True

