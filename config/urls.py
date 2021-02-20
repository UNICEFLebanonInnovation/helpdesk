"""django-helpdesk helpdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from survey.views import IndexView, MapsView, ResearchesView, KnowledgeTrackerList, KnowledgeTrackerChartsView

# The following uses the static() helper function,
# which only works when in development mode (using DEBUG).
# For a real deployment, you'd have to properly configure a media server.
# For more information, see:
# https://docs.djangoproject.com/en/1.10/howto/static-files/

urlpatterns = [
    # url(r'^$', IndexView.as_view(), name='home'),
    url(r'^Dashboard', KnowledgeTrackerChartsView.as_view(), name='dashboard_kmtracker'),
    url(r'^List', KnowledgeTrackerList.as_view(), name='list_kmtracker'),
    # url(r'^Dashboard/Researches/$', ResearchesView.as_view(), name='dashboard_researches'),
    url(r'^', admin.site.urls),
    url(r'^helpdesk', include('helpdesk.urls', namespace='helpdesk')),
    url(r'^survey/', include('survey.urls', namespace='survey')),
    url('i18n/', include('django.conf.urls.i18n')),
    url('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
