# -*- coding: utf-8 -*-
from django.contrib import admin

from translater.models import TranslatedString,OriginalString


class TranslatedStringAdmin(admin.ModelAdmin):
    list_display = ['translated','To']

admin.site.register(TranslatedString,TranslatedStringAdmin)


class OriginalStringAdmin(admin.ModelAdmin):
    list_display = ['original','alreadyTranslated']

    filter_horizontal =['translations']

admin.site.register(OriginalString,OriginalStringAdmin)
