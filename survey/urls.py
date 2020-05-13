from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

app_name = 'survey'

urlpatterns = [

    url(
        r'^home/$',
        views.IndexView.as_view(),
        name='home'
    ),
]
