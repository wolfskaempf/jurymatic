from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

import jurycore.views.protected_views.booklets
import jurycore.views.public_views
from jurycore.views.auth import sign_up;
from jurycore.views.protected_views import overview, booklets, delegates, committees, delegations

app_name = 'jurycore'
urlpatterns = [
    path('', jurycore.views.public_views.home, name='home'),
    path('legend/', TemplateView.as_view(template_name="jurycore/help/legend.html"), name='legend'),
    path('dashboard/', overview.dashboard, name='dashboard'),
    #  Booklets
    path('booklet/create/', booklets.booklet_create, name='booklet_create'),
    path('booklet/<slug:slug>/', booklets.booklet_show, name='booklet_show'),
    path('booklet/<slug:slug>/update/', booklets.booklet_update, name='booklet_update'),
    path('booklet/<slug:slug>/share/', booklets.booklet_share, name='booklet_share'),
    path('booklet/<slug:slug>/share/revoke/<str:username>/', booklets.booklet_revoke_access,
         name='booklet_revoke_access'),
    path('booklet/<slug:slug>/delete/', booklets.booklet_delete, name='booklet_delete'),
    path('booklet/<slug:booklet>/print/', jurycore.views.protected_views.booklets.booklet_print, name='printing_view'),
    #  Delegates
    path('booklet/<slug:booklet>/delegates/', delegates.delegate_list, name='delegate_list'),
    path('booklet/<slug:booklet>/delegate/create/', delegates.delegate_create, name='delegate_create'),
    path('booklet/<slug:booklet>/delegate/register/<uuid:uuid>/', delegates.delegate_register,
         name='delegate_register'),
    path('booklet/<slug:booklet>/delegate/<uuid:uuid>/delete/', delegates.delegate_delete, name='delegate_delete'),
    path('booklet/<slug:booklet>/delegate/<uuid:uuid>/update/', delegates.delegate_update, name='delegate_update'),
    #  Committees
    path('booklet/<slug:booklet>/committees/', committees.committee_list, name='committee_list'),
    path('booklet/<slug:booklet>/committee/<uuid:uuid>/', committees.committee_show, name='committee_show'),
    path('booklet/<slug:booklet>/committee/<uuid:uuid>/update/', committees.committee_update, name='committee_update'),
    path('booklet/<slug:booklet>/committee/<uuid:uuid>/delete/', committees.committee_delete, name='committee_delete'),
    path('booklet/<slug:booklet>/committee/create/', committees.committee_create, name='committee_create'),
    #  Delegations
    path('booklet/<slug:booklet>/delegations/', delegations.delegation_list, name='delegation_list'),
    path('booklet/<slug:booklet>/delegation/<uuid:uuid>/', delegations.delegation_show, name='delegation_show'),
    path('booklet/<slug:booklet>/delegation/<uuid:uuid>/update/', delegations.delegation_update,
         name='delegation_update'),
    path('booklet/<slug:booklet>/delegation/<uuid:uuid>/delete/', delegations.delegation_delete,
         name='delegation_delete'),
    path('booklet/<slug:booklet>/delegation/create/', delegations.delegation_create, name='delegation_create'),
    #  Authentication
    path('sign_up/', sign_up.sign_up, name='sign_up'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
