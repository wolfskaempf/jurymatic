from django.contrib import admin

# Register your models here.

from .models import Committee, Delegate, Delegation

class CommitteeAdmin(admin.ModelAdmin):
    # The information, which should be displayed in the list of committees.
    list_filter = ["name"]

class DelegateAdmin(admin.ModelAdmin):
    # The information, which should be displayed in the list of committees.
    list_display = ("name", "committee", "delegation", "photo")
    list_filter = ["committee__name", "delegation__name"]
    search_fields = ["name", "committee__name", "delegation__name", "photo"]
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(Delegate, DelegateAdmin)
