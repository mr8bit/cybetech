from django.contrib import admin

from .models import *


# Register your models here.
class Social(admin.TabularInline):
    model = Social
    extra = 0
    suit_classes = 'suit-tab suit-tab-social'


class ContactsAdmin(admin.ModelAdmin):
    inlines = (Social,)
    fieldsets = [
        ('Основная информация', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'phone', 'email', 'address', 'telegram',
            ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-social',),
            'fields': []}),
    ]
    suit_form_tabs = (('general', 'Основные'),
                      ('social', 'Cоц. Сети'),)


admin.site.register(Contacts, ContactsAdmin)


# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'name', 'tagline', 'cssClass',
                'type', 'category'
            ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-img',),
            'fields': ['img',],
        }),

    ]
    suit_form_tabs = (('general', 'Основные'),
                      ('img', 'Изображение'),)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Type)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(RecentlyInWork)
