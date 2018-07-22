from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

import jurycore.views.public_views
from jurycore.views import protected_views

app_name = 'jurycore'
urlpatterns = [
    path('', jurycore.views.public_views.home, name='home'),
    path('dashboard/', protected_views.dashboard, name='dashboard'),
    path('booklet/<slug:slug>/', protected_views.booklet_show, name='booklet_show'),
    path('delegate_create/', protected_views.delegate_create, name='delegate_create'),
    path('booklet/<slug:booklet>/committees/', protected_views.committee_list, name='committee_list'),
    path('booklet/<slug:booklet>/committee/<uuid:uuid>/', protected_views.committee_show, name='committee_show'),
    path('booklet/<slug:booklet>/delegation/<uuid:uuid>/', protected_views.delegation_show, name='delegation_show'),
    path('print/', protected_views.printing_view, name='printing_view'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
