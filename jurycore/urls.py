from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'jurycore'
urlpatterns = [
    path('', views.home, name='home'),
    path('delegate_create', views.delegate_create, name='delegate_create'),
    path('committees', views.committee_list, name='committee_list'),
    path('committee/<int:pk>/', views.committee_show, name='committee_show'),
    path('delegation/<int:pk>/', views.delegation_show, name='delegation_show'),
    path('print/', views.printing_view, name='printing_view'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
