from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^committees$', views.committee_list, name='committee_list'),
    url(r'^committee/(?P<pk>\d+)/$', views.committee_show, name='committee_show'),
    url(r'^delegation/(?P<pk>\d+)/$', views.delegation_show, name='delegation_show'),
    url(r'^print/$', views.printing_view, name='printing_view'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
