# -*- coding: utf-8 -*-
from django import template
from translater.models import OriginalString,TranslatedString
from django.conf import settings
from django.utils.encoding import smart_str,smart_unicode
register = template.Library()
import hashlib
from translater.models import OriginalString

#TODO: make tests...
#TODO: add doc strings..

def TranslateMe(string,toLan):
    #FIXME: Just convert everything to utf-8
    try:
        inPut=smart_str(string)
    except:
        inPut=smart_unicode(string)


    ident = hashlib.md5(inPut).hexdigest()

    original,created = OriginalString.objects.get_or_create(ident=ident)

    if created:
        original.original = string
        original.save()
        return original.original
    else:
        trans =original.translations.select_related().filter(To=toLan)
        if trans:
            #FIXME: create a ger_or_none method...
            return trans[0]

        else:
            #TODO: Run thread in bg to get translater from google.
            return inPut




register.filter(TranslateMe)
