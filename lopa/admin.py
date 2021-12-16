from django.contrib import admin
from django.contrib.auth.admin import Group
from .models import Project, Event, Cause, Cause_Barrier, Consequence, Consequence_Barrier


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("name", )
    search_fields = ("name", )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("description", "target_frequency", "project")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("description",)
    search_fields = ("description",)


@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    list_display = ("description", "initial_frequency", "event")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("description",)
    search_fields = ("description",)


@admin.register(Cause_Barrier)
class Cause_BarrierAdmin(admin.ModelAdmin):
    list_display = ( "description", "pfd", "cause")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("description",)
    search_fields = ("description",)


@admin.register(Consequence)
class ConsequenceAdmin(admin.ModelAdmin):
    fields = ("description", "event", "target_frequency", "project")
    list_display = ("description", "target_frequency", "event")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("description",)
    search_fields = ("description",)

@admin.register(Consequence_Barrier)
class Consequence_BarrierAdmin(admin.ModelAdmin):
    list_display = ("description", "pfd", "consequence")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("consequence",)
    list_filter = ("description",)
    search_fields = ("description",)


admin.site.unregister(Group)
