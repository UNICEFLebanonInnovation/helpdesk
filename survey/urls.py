from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

app_name = 'survey'

urlpatterns = [

    url(
        r'^Dashboard/Maps/$',
        views.IndexView.as_view(),
        name='dashboard_maps'
    ),

    url(
        r'^Dashboard/Researches/$',
        views.IndexView.as_view(),
        name='dashboard_researches'
    ),
    url(
        r'^feedback-select-view/$',
        view=views.FeedbackSelectView,
        name='feedback-select-view'
    ),
    url(
        r'^feedback-update-view/$',
        view=views.FeedbackUpdateView,
        name='feedback-update-view'
    ),


]
