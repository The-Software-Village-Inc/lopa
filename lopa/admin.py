from django.contrib import admin
from .models import Consequence, Consequence_Barrier, Project, Event, Cause, Cause_Barrier; Consequence, Consequence_Barrier

admin.site.register(Project)
admin.site.register(Event)
admin.site.register(Cause)
admin.site.register(Cause_Barrier)
admin.site.register(Consequence)
admin.site.register(Consequence_Barrier)
