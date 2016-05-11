from django.contrib import admin

# Register your models here.

from .models import Committee, Delegate, Delegation

class CommitteeAdmin(admin.ModelAdmin):
    # The information, which should be displayed in the list of committees.
    list_filter = ["name"]
admin.site.register(Committee, CommitteeAdmin)
