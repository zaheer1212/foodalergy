from django.contrib import admin

from blog.models import Entry

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"entrySlug": ("entryTitle",)}

admin.site.register(Entry, EntryAdmin)
