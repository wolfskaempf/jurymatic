from django.contrib import admin

# Register your models here.
from guardian.admin import GuardedModelAdmin

from .models import Committee, Delegate, Delegation


class CommitteeAdmin(GuardedModelAdmin):
    # The information, which should be displayed in the list of committees.
    list_filter = ["name"]


class DelegateAdmin(GuardedModelAdmin):
    # The information, which should be displayed in the list of committees.
    list_display = ("name", "committee", "delegation", "photo")
    list_filter = ["committee__name", "delegation__name"]
    search_fields = ["name", "committee__name", "delegation__name", "photo"]


class DelegationAdmin(GuardedModelAdmin):
    # The information, which should be displayed in the list of committees.
    list_filter = ["name"]


admin.site.register(Committee, CommitteeAdmin)
admin.site.register(Delegate, DelegateAdmin)
admin.site.register(Delegation, DelegationAdmin)
