from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

import jurycore.views.public_views
from jurycore.views.auth import sign_up;
from jurycore.views.protected_views import overview, booklets, delegates, committees, delegations, printing

app_name = 'jurycore'
urlpatterns = [
    path('', jurycore.views.public_views.home, name='home'),
    path('dashboard/', overview.dashboard, name='dashboard'),
    path('booklet_create/', booklets.booklet_create, name='booklet_create'),
    path('booklet/<slug:slug>/', booklets.booklet_show, name='booklet_show'),
    path('booklet/<slug:slug>/delete/', booklets.booklet_delete, name='booklet_delete'),
    path('delegate_create/', delegates.delegate_create, name='delegate_create'),
    path('booklet/<slug:booklet>/committees/', committees.committee_list, name='committee_list'),
    path('booklet/<slug:booklet>/committee/<uuid:uuid>/', committees.committee_show, name='committee_show'),
    path('booklet/<slug:booklet>/committee/<uuid:uuid>/update/', committees.committee_update, name='committee_update'),
    path('booklet/<slug:booklet>/committee/<uuid:uuid>/delete/', committees.committee_delete, name='committee_delete'),
    path('booklet/<slug:booklet>/committee/create/', committees.committee_create, name='committee_create'),
    path('booklet/<slug:booklet>/delegations/', delegations.delegation_list, name='delegation_list'),
    path('booklet/<slug:booklet>/delegation/<uuid:uuid>/', delegations.delegation_show, name='delegation_show'),
    path('booklet/<slug:booklet>/delegation/create/', delegations.delegation_create, name='delegation_create'),
    path('booklet/<slug:booklet>/print/', printing.printing_view, name='printing_view'),
    path('sign_up/', sign_up.sign_up, name='sign_up'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
