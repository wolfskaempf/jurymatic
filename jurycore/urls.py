from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from jurycore.views.protected_views import overview, booklets, delegates, committees, delegations, printing
import jurycore.views.public_views

app_name = 'jurycore'
urlpatterns = [
    path('', jurycore.views.public_views.home, name='home'),
    path('dashboard/', overview.dashboard, name='dashboard'),
    path('booklet_create/', booklets.booklet_create, name='booklet_create'),
    path('booklet/<slug:slug>/', booklets.booklet_show, name='booklet_show'),
    path('delegate_create/', delegates.delegate_create, name='delegate_create'),
    path('booklet/<slug:booklet>/committees/', committees.committee_list, name='committee_list'),
    path('booklet/<slug:booklet>/committee/<uuid:uuid>/', committees.committee_show, name='committee_show'),
    path('booklet/<slug:booklet>/delegation/<uuid:uuid>/', delegations.delegation_show, name='delegation_show'),
    path('booklet/<slug:booklet>/print/', printing.printing_view, name='printing_view'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
