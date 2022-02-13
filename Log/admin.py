from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Logbook)
class LogbookAdmin(admin.ModelAdmin):
    """"
    An admin class for the viewing and editing of the logbok entries
    """
    list_display = ('date', 'task', 'hours_worked')
    fields = ('date', ('task', 'hours_worked'), 'description', "emotion")
