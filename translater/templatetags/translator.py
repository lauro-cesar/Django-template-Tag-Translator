# -*- coding: utf-8 -*-
from django import template
from translater.models import myString
from django.conf import settings
register = template.Library()
import hashlib


def TranslateMe(string,toLan):
    
    ident = hashlib.md5(string).hexdigest()
    translated,created = myString.objects.get_or_create(ident=ident,languageTo=toLan)
    translated.original = string
    translated.save()
    
    if translated.translated:
        return translated.translated
    else:
        return  string


register.filter(TranslateMe)
