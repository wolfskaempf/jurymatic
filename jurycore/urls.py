from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from jurycore.views import protected_views

app_name = 'jurycore'
urlpatterns = [
    path('', protected_views.home, name='home'),
    path('dashboard', protected_views.dashboard, name='dashboard'),
    path('booklet/<str:slug>', protected_views.booklet_show, name='booklet_show'),
    path('delegate_create', protected_views.delegate_create, name='delegate_create'),
    path('committees', protected_views.committee_list, name='committee_list'),
    path('committee/<int:pk>/', protected_views.committee_show, name='committee_show'),
    path('delegation/<int:pk>/', protected_views.delegation_show, name='delegation_show'),
    path('print/', protected_views.printing_view, name='printing_view'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
