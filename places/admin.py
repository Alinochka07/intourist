from django.contrib import admin
from .models import *


admin.site.register(Place)
# admin.site.register(Feedback)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'place', 'text', 'user', 'checked']
    list_editable = ['checked']
    list_filter = ['checked']
    search_fields = ['text', 'place__name', 'place__location', 'place__description']

    fields = ['user', 'place', 'text']
    readonly_fields = ['text']


admin.site.register(Feedback, FeedbackAdmin)