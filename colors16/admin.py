from django.contrib import admin

from .models import Colors

# Register your models here.

# http://www.w3schools.com/html/html_colornames.asp

class ColorsAdmin(admin.ModelAdmin):
    # readonly_fields = ('thumbnail_tag', 'images_tags')
    list_display = ['title', 'translate', 'code', 'color_box']
    readonly_fields = ('color_box', )
    fieldsets = [
        (None, {'fields': ['color_box', 'title', 'alias', 'translate', 'code', ]}),
        # ('Thumbnail', {'fields': ['thumbnail_tag']}),
        # ('Images', {'fields': ['images_tags'], 'classes': ['collapse']}),
    ]

    class Media:
        css = {
            'all': ('css/admin.css',)
        }

admin.site.register(Colors, ColorsAdmin)



