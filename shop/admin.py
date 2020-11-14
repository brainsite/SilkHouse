from django.contrib import admin
from django.template.loader import render_to_string
from sorl.thumbnail.admin import AdminImageMixin


from colors16.models import COLORS_HELP_TABLE
from .models import Scarf

# Register your models here.


class StockFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = u'В продаже'
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'in_stock'
    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('in_stock', u'В наличии'),
            ('on_sale', u'В продаже'),
            ('sold_out', u'Нет в наличии'),
        )
    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'in_stock':
            return Scarf.objects.in_stock()
        if self.value() == 'on_sale':
            return Scarf.objects.on_sale()
        if self.value() == 'sold_out':
            return Scarf.objects.sold_out()


class CheckFilter(admin.SimpleListFilter):
    title = u'Не заполненны'
    parameter_name = 'not completed'
    def lookups(self, request, model_admin):
        return (
            ('no_price', u'Нет цены'),
            ('no_weight', u'Нет веса'),
            ('no_colors', u'Нет цвета'),
            ('no_photo', u'Нет фото'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'no_price':
            return queryset.filter(price__lte=0)
        if self.value() == 'no_weight':
            return queryset.filter(weight__lte=0)
        if self.value() == 'no_colors':
            return queryset.exclude(l_color__isnull=False)
        if self.value() == 'no_photo':
            return queryset.exclude(img__isnull=False)


# class ScarfInlineModelAdmin(AdminImageMixin, admin.TabularInline):

class ScarfAdmin(AdminImageMixin, admin.ModelAdmin):
    #
    # # Для админки

    def color_table_help(self, obj):
        u"""
        Рисуем статичную табличку в shop.admin.scarf
        """
        return COLORS_HELP_TABLE
    color_table_help.short_description = 'Таблица Цветов'
    color_table_help.allow_tags = True
    #
    # # Для админки отображения в списке
    # def get_l_color(self):
    #     u"""
    #     shop.admin.list_view возвращает имя цвета или пустою строку.
    #     """
    #     if self.l_color:
    #         return self.l_color.translate
    #     else:
    #         return ''
    # get_l_color.short_description = 'L Color'
    #
    # def get_s_colors(self):
    #     u"""
    #     shop.admin.list_view возвращает значения через запятую или пустою строку.
    #     """
    #     return ", ".join([x.translate for x in self.s_color.all()])
    # get_l_color.short_description = 'S Color'

    def thumb(self, obj):
        return render_to_string('thumb.html', {'img': obj.img})
    thumb.allow_tags = True
    thumb.short_description = 'Фото'

    list_display = ['id',
                    'thumb',
                    'title',
                    'count',
                    'price',
                    'weight',
                    # 'get_l_color',
                    # 'get_s_colors',
                    'hide',
                    'multicolor',
                    ]
    readonly_fields = ('color_table_help', 'multicolor', )
    # readonly_fields = ('multicolor', )
    fieldsets = [
        (None, {'fields': ['img', 'title', 'count', 'price', 'weight', ('hide', ), ]}),
        # ('Colors', {'fields': ['color_table_help', 'l_color', 's_color', 'male', ]}),
        ('Colors', {'fields': ['l_color', 's_color', 'male' ],
                    'classes': ['collapse']}),
        # ('Thumbnail', {'fields': ['thumbnail_tag']}),
        # ('Images', {'fields': ['images_tags'], 'classes': ['collapse']}),
    ]

    list_filter = (CheckFilter, StockFilter, 'l_color', 's_color')
    # 'l_color', 's_color')


admin.site.register(Scarf, ScarfAdmin)