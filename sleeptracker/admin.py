from django.contrib import admin
from sleeptracker.models import SleepState

class SleepStateAdmin(admin.ModelAdmin):
    #list_display = ('date', 'user', 'state')
    pass

admin.site.register(SleepState, SleepStateAdmin)
