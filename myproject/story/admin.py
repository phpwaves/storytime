from django.contrib import admin
from story.models import ZomatoItem, Line, Choices

admin.site.register(ZomatoItem)
admin.site.register(Line)
class ChoicesAdmin(admin.ModelAdmin):
	list_display = ('parent','description')
	list_filter = ('parent','description')

admin.site.register(Choices, ChoicesAdmin)
